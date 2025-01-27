from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

connection_string = os.getenv('MONGODB_URI')

# Connect to your MongoDB Atlas cluster
client = MongoClient(connection_string)

# Select your database and collection
db = client["aws_spot_prices_db"]
collection = db["aws_spot_prices"]

# Get all unique values for the field
unique_values = collection.distinct("region")

# Print the unique values
print(unique_values)
