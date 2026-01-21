import os

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
model = ChatOpenAI(
    model='glm-4.7',
    api_key=os.getenv("API_KEY"),
    base_url=os.getenv("BASE_URL"))

