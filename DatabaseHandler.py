import asyncio
import discord
import time
import threading

from dotenv import load_dotenv
from os import getenv
from pymongo import MongoClient





class DiscordDB(discord.Client):
    
    def __init__(self):
        
        super().__init__(intents = discord.Intents.all())
        
        load_dotenv()
        
        # asyncio.run(self.__initiateDiscordDB())



    def initiateDiscordDB(self):
        
        self.test_environment = True
        self.discord_token = getenv('DISCORD_TOKEN')
        
        self.run(self.discord_token)
        # await self.start(self.discord_token)
        # await self.start(self.discord_token)
    
    

    async def on_ready(self):
        
        self.channel_file_server = self.get_channel(int(getenv('CHANNEL_FILE_SERVER')))
        self.channel_test = self.get_channel(int(getenv('CHANNEL_TEST')))
        self.channel_webhook = self.get_channel(int(getenv('CHANNEL_WEBHOOK')))
        
        if self.test_environment:
            self.channel_default = self.channel_test
        else:
            self.channel_default = self.channel_file_server
        
        current_time = time.time()
        message = discord.Embed(title = "App was initialized...", description = f"Was initialized at {int(((current_time // (60 * 60)) + 3) % 24)}:{int((current_time // 60) % 60)}:{int(current_time % 60)}", color = 0x00ddaa)
        message.set_footer(text = "Initialized by Afraaz")
        # message_id = await self.channel_default.send(f"Was booted at {time.time()} by Afraaz")
        message_id = await self.channel_default.send(embed = message)
        
        # print(f"Bot is online! Message ID: {message_id.id}")
        
        await self.change_presence(activity = discord.Game(name = "with your data"))



    async def uploadData(self, data):
        
        message = discord.Embed(title = "Data was uploaded...", description = f"Data was uploaded at {time.time()}", color = 0x00ddaa)
        message.add_field(name = "Data", value = data)
        message.set_footer(text = "Uploaded by Afraaz")
        message_id = await self.channel_default.send(embed = message)
        
        return message_id.id
    
    
    
    async def retrieveData(self, data):
        ...
    
    
    
    async def deleteData(self, data):
        ...





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
        
    
    
    
    def updateUser(self, data):
        ...
    
    
    
    def deleteUser(self, username):
        
        return self.collection.delete_one({'username': username})
    
    
    
    def banUser(self, username):
        ...
