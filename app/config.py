import os

user = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")
database = os.getenv("MYSQL_DATABASE")
database_url = os.getenv("DATABASE_URL")

SECRET_KEY = os.getenv("SECRET_KEY")

SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{user}:{password}@{database_url}/{database}"
SQLALCHEMY_TRACK_MODIFICATIONS = False