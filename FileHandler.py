from DatabaseHandler import DiscordDB, MongoDB





class FileHandler(MongoDB):
    
    def __init__(self):
        
        super().__init__()
    
    
    
    def __encryptFragment(self, fragment):
        ...
    
    
    
    def __encryptFile(self, file):
        ...
    
    
    
    def __decryptFragment(self, fragment):
        ...
    
    
    
    def __decryptFile(self, file):
        ...
    
    
    
    def __hashText(self, text):
        ...
    
    
    
    def uploadFile(self, file):
        ...
    
    
    
    def retrieveFile(self, file):
        ...
    
    
    
    def deleteFile(self, file):
        ...





def initiate():
    
    interface = FileHandler()





if __name__ == '__main__':
    
    try:
        initiate()
    except Exception as error:
        pass