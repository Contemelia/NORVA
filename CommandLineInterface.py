import asyncio

from FileHandler import FileHandler
from os import system





class Interactions(FileHandler):
    
    def __init__(self):
        
        super().__init__()
        
        
        self.options = {
            'a': self.__create,
            'b': self.__login,
            'c': self.__update,
            'd': self.__delete,
            'e': self.__ban
        }
        
        # self.initiateProcess()
    
    
    
    async def __clearConsole(self):
        await system('cls')
        print("NOルVA v1.0b")
        print("Author: 列星氷刃")
    
    
    
    def __hashText(self, text):
        return super().__hashText(text)
    
    
    
    def __create(self, payload):
        
        self.__clearConsole()
        
        payload = {}
        
        payload['username'] = input('Enter username: ')
        payload['password'] = input('Enter password: ')
        payload['display_name'] = input('Enter display name: ')
        
        return super().createUser(payload)
    
    
    
    def __login(self):
        
        self.__clearConsole()
        
        payload = {}
        
        payload['username'] = input('Enter username: ')
        payload['password'] = input('Enter password: ')
        
        return super().loginUser(payload)
    
    
    
    def __update(self, payload):
        
        self.__clearConsole()
        
        payload = {}
        
        payload['username'] = input('Enter username: ')
        payload['password'] = input('Enter password: ')
        payload['display_name'] = input('Enter display name: ')
        
        return super().updateUser(payload)
    
    
    
    def __delete(self):
        
        self.__clearConsole()
        
        username = input('Enter username: ')
        password = input('Enter password: ')
        
        return super().deleteUser(username, password)

    
    
    def __ban(self):
        
        self.__clearConsole()
        
        username = input('Enter username: ')
        
        return super().banUser(username)
    
    
    
    async def initiateProcess(self):
        
        while True:
            
            await self.__clearConsole()
            
            print('''Select an option...
                  
            A. Create user
            B. Login user
            C. Update user
            D. Delete user
            
            ''')
            
            option = input('Enter option: ').lower()
            
            if option in self.options:
                await self.options[option]()
            else:
                print('\nInvalid option')
                break





# async def initiate():
    
#     interactions = await Interactions()
#     # interactions.initiateProcess()





# if __name__ == '__main__':
    
#     try:
#         initiate()
#     except Exception as error:
#         pass

# Interactions()

Interactions = Interactions()
asyncio.run(Interactions.initiateProcess())