# python环境要求
```bash
pip install -r requirements.txt
```
# 配置环境变量

创建 `.env`文件，在.env文件中的设置 `MODEL_NAME`,`API_KEY` 和 `BASE_URL` 为自己的 key 和 url
使用openai API时，需要配置base url
`LANGCHAIN_TRACING_V2`设置为true，`LANGCHAIN_PROJECT`设置为项目名称，不配置默认为default，`LANGCHAIN_API_KEY`设置为LangSmith的API Key，可以在LangSmith中查看调用大模型使用情况，不需要也可以不配置这两个变量

## langsmith的检测数据
配置`LANGCHAIN_TRACING_V2`，`LANGCHAIN_API_KEY`后可以在https://smith.langchain.com/ Tracing Projects中查看调用大模型的使用情况


## 魔搭社区向量数据库介绍
https://www.modelscope.cn/models/iic/nlp_gte_sentence-embedding_chinese-large/summary