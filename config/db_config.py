import certifi
from pymongo import MongoClient

MONGO_API = "mongodb+srv://arpitChokniwal:arpitChokniwal@cluster0.gkdcufn.mongodb.net/"
My_Client = MongoClient(MONGO_API, tlsCAFile=certifi.where())
My_Database = My_Client['All_Data']
My_Collection = My_Database["addresses"]
