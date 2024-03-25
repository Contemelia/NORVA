import discord

# from discord_slash import SlashCommand
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv





class DiscordDB(discord.Client):
    
    def __init__(self):
        
        super().__init__(intents = discord.Intents.all())
        # SlashCommand(self, sync_commands = True)
        
        load_dotenv()
        
        self.__initiateDiscordDB()



    def __initiateDiscordDB(self):
        
        self.test_environment = True
        self.discord_token = getenv('DISCORD_TOKEN')
        
        self.run(self.discord_token)
    
    

    # @self.event
    async def on_ready(self):
        
        self.channel_file_server = self.get_channel(int(getenv('CHANNEL_FILE_SERVER')))
        self.channel_test = self.get_channel(int(getenv('CHANNEL_TEST')))
        self.channel_webhook = self.get_channel(int(getenv('CHANNEL_WEBHOOK')))
        
        if self.test_environment:
            self.channel_default = self.channel_test
        else:
            self.channel_default = self.channel_file_server
        
        # message_id = await self.channel_default.send("I am online!")
        # print(f"Bot is online! Message ID: {message_id.id}")
        
        try:
            await self.tree.sync()
        except Exception as error:
            pass
        
        await self.change_presence(activity = discord.Game(name = "with your data"))



    async def uploadData(self, data):
        ...
    
    
    
    async def retrieveData(self, data):
        ...
    
    
    
    async def deleteData(self, data):
        ...





class MongoDB():
    
    def __init__(self):
        
        load_dotenv()
        
        self.__initiateMongoDB()
    
    
       
    def __initiateMongoDB(self):
        
        self.mongodb_token = getenv('MONGODB_TOKEN')
        print(self.mongodb_token)
    
    
    
    def createUser(self, payload):
        ...
    
    
    
    def loginUser(self, username, password):
        ...
    
    
    
    def updateUser(self, data):
        ...
    
    
    
    def deleteUser(self, username, password):
        ...
    
    
    
    def banUser(self, username):
        ...




def initiateScript():
    
    an_object = MongoDB()





if __name__ == "__main__":
    
    try:
        initiateScript()
    except KeyboardInterrupt:
        pass