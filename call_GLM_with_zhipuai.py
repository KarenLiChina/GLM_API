import os

from dotenv import load_dotenv
from zhipuai import ZhipuAI

# 使用GLM自己的API

load_dotenv()
client = ZhipuAI(api_key=os.getenv("API_KEY"))

response = client.chat.completions.create(
    model='glm-4.7',
    messages=[
        {'role': "users", 'content': '请介绍下GLM的发展历史。'}
    ],
    stream=False  # 默认值是false，是否按照流式输出
)

print(response)
print(response.choices[0].message.content)
