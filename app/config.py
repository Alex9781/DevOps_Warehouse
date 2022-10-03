import os

user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DATABASE")

SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{user}:{password}@database/{database}"
SQLALCHEMY_TRACK_MODIFICATIONS = False
