import pandas as pd
import mysql.connector as mysql_con
import pyodbc
import sqlalchemy
from sqlalchemy.engine import URL


DATA_FILE_PATH = "data/accounts.csv"

HOST = "localhost"

USER_NAME = "root"

PASSWORD = "@n1m34l1f3"

DATABASE_SCHEMA_NAME = "py_db_schema"

TABLE_NAME = "accounts"


accounts = pd.read_csv(
	filepath_or_buffer=DATA_FILE_PATH,
	engine="c",
	low_memory=False
)

mysql_connection_url = URL.create(
	"mysql+pymysql",
	username=USER_NAME,
	password=PASSWORD,
	host=HOST,
	database=DATABASE_SCHEMA_NAME
)

mysql_connection_engine = sqlalchemy.create_engine(mysql_connection_url)

accounts.to_sql(
	name=TABLE_NAME,
	con=mysql_connection_engine,
	if_exists="replace",
	index=False
)