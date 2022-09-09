from pymongo import MongoClient
from dotenv import dotenv_values

config = dotenv_values(".env")

MONGO_URI = f'mongodb://{config["MONGO_USER"]}:{config["MONGO_PASS"]}@mongo:27017/?authMechanism={config["MONGO_DB"]}'

conn = MongoClient(MONGO_URI)

db = conn[config["MONGO_DB"]]
User = db.user
Vacancy = db.vacancy