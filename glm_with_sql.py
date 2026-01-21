import os

from langchain_classic.chains.sql_database.query import create_sql_query_chain
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI

HOSTNAME = os.getenv("MYSQL_HOSTNAME")
PORT = os.getenv("MYSQL_PORT")
DATABASE = os.getenv("MYSQL_DATABASE")
USERNAME = os.getenv("MYSQL_USERNAME")
PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_URI = 'mysql+mysqldb://{}:{}@{}:{}/{}?charset=utf8mb4'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

db_connection = SQLDatabase.from_uri(MYSQL_URI)
print(db_connection.dialect)
print(db_connection.get_usable_table_names())
print(db_connection.run('select * from t_emp;'))
model = ChatOpenAI(
    model='glm-4.7',
    api_key=os.getenv("API_KEY"),
    base_url=os.getenv("BASE_URL"))

chain = create_sql_query_chain(llm=model, db=db_connection)
# chain.get_prompts()[0].pretty_print()# 此时Chain中自带了内置的prompt,可以打印出来
resp = chain.invoke({'question': '请问：一共有多少员工？'})
print('LLM生成的SQL:'+resp)
sql=resp.replace('```sql','').replace('```','')
print('提取之后的sql：'+sql)
print(db_connection.run(sql))