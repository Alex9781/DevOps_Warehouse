import os
user = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")
database = os.getenv("MYSQL_DATABASE")

SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{user}:{password}@database/{database}"
SQLALCHEMY_TRACK_MODIFICATIONS = False