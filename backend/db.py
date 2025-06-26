from pymongo import MongoClient

# Replace with your actual MongoDB URI
MONGO_URI = "mongodb://localhost:27017"
client = MongoClient(MONGO_URI)

# Use or create database and collection
db = client["secure_file_share"]
metadata_collection = db["file_metadata"]
