import os
from dotenv import load_dotenv
load_dotenv()

# MySQL setup
MYSQL_USERNAME = os.getenv('MYSQL_USERNAME')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_HOST = os.getenv('MYSQL_HOST')
MYSQL_PORT = os.getenv('MYSQL_PORT')
MYSQL_DB1 = os.getenv('MYSQL_DB1')
MYSQL_DB2 = os.getenv('MYSQL_DB2')

SQLALCHEMY_DATABASE_URL1  = f'mysql+mysqlconnector://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB1}'
SQLALCHEMY_DATABASE_URL2  = f'mysql+mysqlconnector://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB2}'


# Log file path
LOG_FILE_PATH1 = os.getenv('LOG_FILE_PATH1')
LOG_FILE_PATH2 = os.getenv('LOG_FILE_PATH2')

