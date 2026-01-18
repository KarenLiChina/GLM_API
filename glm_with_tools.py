import csv
import os
from typing import Type, Optional

import requests
from dotenv import load_dotenv
from langchain_core.callbacks import CallbackManagerForToolRun
from langchain_core.messages import HumanMessage
from langchain_core.tools import BaseTool
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import chat_agent_executor
from pydantic import BaseModel, Field

load_dotenv()

bai_du_ak = os.getenv("BAI_DU_AK")


def find_code(csv_file_path, district_name) -> str:
    """
    根据区域或者城市的名字，返回该区域的编码
    :param csv_file_path:
    :param district:
    :return:
    """
    district_map = {}
    with open(csv_file_path, mode='r', encoding='utf-8') as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            district_code = row['district_id']
            district = row['district']
            if district not in district_map:
                district_map[district] = district_code
    return district_map.get(district_name, None)


class WeatherInputArgs(BaseModel):
    """
    Input的Schema类
    """
    location: str = Field(..., description="用于查询天气的位置信息")  # description 要写好，给大模型来看的


class WeatherTool(BaseTool):
    """
    查询实时天气的工具
    """
    name: str = 'weather_tool'
    description: str = '可以查询任意位置的当前天气情况'
    args_schema: Type[WeatherInputArgs] = WeatherInputArgs

    def _run(self,
             location: str,
             run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        """调用工具的时候，自动执行的函数"""
        district_code = find_code('./data/weather_district_id.csv', location)
        print(f'需要查询的{location} 的地区编码是{district_code}')

        url = f'https://api.map.baidu.com/weather/v1/?district_id={district_code}&data_type=now&ak={bai_du_ak}'

        # 发送请求
        response = requests.get(url=url)
        data = response.json()
        text = data['result']['now']['text']
        temp = data['result']['now']['temp']
        feels_like = data['result']['now']['feels_like']
        rh = data['result']['now']['rh']
        wind_dir = data['result']['now']['wind_dir']
        wind_class = data['result']['now']['wind_class']

        return f"位置：{location} 当前天气：{text}，温度：{temp}℃，体感温度：{feels_like}℃，相对湿度：{rh}%，{wind_dir}：{wind_class}"


if __name__ == '__main__':
    model = ChatOpenAI(
        model='glm-4.7',
        temperature=0.6,
        api_key=os.getenv("API_KEY"),
        base_url=os.getenv("BASE_URL"))

    tools = [WeatherTool()]

    agent_executor = chat_agent_executor.create_tool_calling_executor(model, tools)

    resp = agent_executor.invoke({'messages': [HumanMessage(content='中国的首都是哪个城市？')]})
    print(resp['messages'])

    resp2 = agent_executor.invoke({'messages': [HumanMessage(content='北京天气怎么样？')]})
    print(resp2['messages'])

    print(resp2['messages'][2].content)
