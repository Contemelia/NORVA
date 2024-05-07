import asyncio
import time
import threading

from dotenv import load_dotenv
from os import getenv
from pymongo import MongoClient






class MongoDB():
    
    def __init__(self, token = None):
        
        load_dotenv()
        
        self.mongodb_token = token
        
        self.__initiateMongoDB()
    
    
       
    def __initiateMongoDB(self):
        
        self.client = MongoClient(self.mongodb_token)
        self.collection = self.client.user_data.user_data
    
    
    
    def checkExistance(self, username):
        
        return True if self.collection.find_one({'username': username}) else False
    
    
    
    def createUser(self, payload):
        
        return self.collection.insert_one(payload)
    
    
    
    def retrieveUser(self, username):
        
        return self.collection.find_one({'username': username})
    
    
    
    def updateDisplayName(self, username, display_name):
        
        return self.collection.update_one({'username': username}, {'$set': {'display_name': display_name}})
    
    
    
    def uploadFile(self, username, file, consumed_storage):
        
        return self.collection.update_one({'username': username}, {'$set': {'consumed_storage': consumed_storage, 'files': file}})
    
    
    
    def deleteUser(self, username):
        
        return self.collection.delete_one({'username': username})
    
    
    
    def banUser(self, username):
        ...