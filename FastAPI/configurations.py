from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import certifi

# mongoDB URI here
uri = "mongodb+srv://<username>:<password>@cluster0.hwwszmk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, tlsCAFile=certifi.where())

db = client.todo_db
collection = db["todo_data"]