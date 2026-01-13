import os

from dotenv import load_dotenv
from openai import OpenAI

# 使用OpenAI的API

load_dotenv()
client = OpenAI(api_key=os.getenv("API_KEY"),
                base_url=os.getenv("BASE_URL"))

response = client.chat.completions.create(
    model='glm-4.7',
    messages=[
        {'role': "users", 'content': '请介绍下GLM的发展历史。'}
    ],
    stream=True  # 默认值是false，是否按照流式输出
)

# 流式输出
for s in response:
    print(s.choices[0].delta)
