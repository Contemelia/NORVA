from dotenv import load_dotenv
from hashlib import sha256
from os import getenv

from DatabaseHandler import MongoDB





class DataHandler():
    
    def __init__(self):
        
        load_dotenv()
        
        mongodb_token = getenv('MONGODB_TOKEN')
        
        self.MongoDB = MongoDB(mongodb_token)    
    
    
    
    def __encryptFragment(self, fragment):
        ...
    
    
    
    def __encryptFile(self, file):
        ...
    
    
    
    def __decryptFragment(self, fragment):
        ...
    
    
    
    def __decryptFile(self, file):
        ...
    
    
    
    def __hashText(self, text):
        
        return sha256(text.encode()).hexdigest()
    
    
    
    def uploadFile(self, file, credentials):
        ...
    
    
    
    def retrieveFile(self, file):
        ...
    
    
    
    def deleteFile(self, file, credentials):
        ...
    
    
    
    def createAccount(self, credentials):
        
        username = credentials['username'].lower()
        password = credentials['password']
        display_name = credentials['display_name']
        
        username_hash = self.__hashText(username)
        password_hash = self.__hashText(password)
        
        payload = {
            'username': username_hash, 
            'password': password_hash, 
            'display_name': display_name, 
            'standing': 10.0, 
            'status': 'active', 
            'allowed_storage': 5120, 
            'consumed_storage': 0, 
            'files': []
        }
        
        if not self.MongoDB.checkExistance(username_hash):
            self.MongoDB.createUser(payload)
            return self.MongoDB.retrieveUser(username_hash)
        else:
            return '1'
    
    
    
    def loginAccount(self, credentials):
            
            username = credentials['username'].lower()
            password = credentials['password']
            
            username_hash = self.__hashText(username)
            password_hash = self.__hashText(password)
            
            if self.MongoDB.checkExistance(username_hash):
                user_credentials = self.MongoDB.retrieveUser(username_hash)
                
                if user_credentials['password'] == password_hash:
                    if user_credentials['status'] == 'suspended':
                        return '3'
                    return user_credentials
                else:
                    return '1'
            else:
                return '2'
    
    
    
    def deleteAccount(self, credentials):
        
        username = credentials['username'].lower()
        password = credentials['password']
        
        username_hash = self.__hashText(username)
        password_hash = self.__hashText(password)
        
        if self.MongoDB.checkExistance(username_hash):
            user = self.MongoDB.retrieveUser(username_hash)
            
            if user['password'] == password_hash:
                self.MongoDB.deleteUser(username_hash, password_hash)
            else:
                return '1'
        else:
            return '2'





def initiate():
    
    interface = DataHandler()





if __name__ == '__main__':
    
    try:
        initiate()
    except Exception as error:
        pass