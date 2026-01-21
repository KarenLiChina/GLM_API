# python环境要求
```bash
pip install -r requirements.txt
```
# 配置环境变量

创建 `.env`文件，在.env文件中的设置 `MODEL_NAME`,`API_KEY` 和 `BASE_URL` 为自己的 key 和 url
`BAI_DU_AK`设置为百度天气查询的AK
`LANGCHAIN_TRACING_V2`设置为true，`LANGCHAIN_PROJECT`设置为项目名称，不配置默认为default，`LANGCHAIN_API_KEY`设置为LangSmith的API Key，可以在LangSmith中查看调用大模型使用情况，不需要也可以不配置这两个变量

## langsmith的检测数据
配置`LANGCHAIN_TRACING_V2`，`LANGCHAIN_API_KEY`后可以在https://smith.langchain.com/ Tracing Projects中查看调用大模型的使用情况

## 通过智谱自己的API调用
call_GLM_with_zhipuai.py

## 通过openai的API调用
call_GLM_with_openai.py

# 通过langchain调用
call_GLM_with_langchain.py

## 通过魔搭社区的向量模型进行向量化
call_GLM_embeddings.py

### 魔搭社区向量模型数据库介绍
https://www.modelscope.cn/models/iic/nlp_gte_sentence-embedding_chinese-large/summary

## GML使用工具
glm_with_tools.py
### 百度天气查询API介绍
https://lbs.baidu.com/faq/api?title=webapi/weather/base
测试url：
curl "https://api.map.baidu.com/weather/v1/?district_id=110100&data_type=now&ak=你的ak"


## GML整合数据库操作
流程：
Prompt -> LLM -> SQL -> Function -> DB执行 -> Prompt -> LLM -> Result

### MySQL配置
在.env 文件中配置自己的mysql配置：`MYSQL_HOSTNAME`,`MYSQL_PORT`,`MYSQL_DATABASE`,`MYSQL_USERNAME`,`MYSQL_PASSWORD`
