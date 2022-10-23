import os

user = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")
database = os.getenv("MYSQL_DATABASE")

SECRET_KEY = os.getenv("SECRET_KEY")

SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{user}:{password}@192.168.88.102/{database}"
SQLALCHEMY_TRACK_MODIFICATIONS = False
