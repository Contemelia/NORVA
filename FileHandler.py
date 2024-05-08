from dotenv import load_dotenv
from hashlib import sha256
from os import getenv, listdir, path, remove
from requests import exceptions, get
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from uuid import uuid4
from datetime import datetime

from DatabaseHandler import MongoDB





class DataHandler():
    
    def __init__(self):
        
        load_dotenv()
        
        mongodb_token = getenv('MONGODB_TOKEN')
        
        self.MongoDB = MongoDB(mongodb_token)   
    
    
    
    # Function to check for internet connection.
    def __checkConnection(self):
        
        try:
            get('http://www.google.com', timeout = 5)
            return True
        except exceptions.RequestException:
            return False
    
    
    
    def __fragmentAndEncrypt(self, file_content, fragment_size, key):
        
        fragment_list, fragment_count = listdir('Data'), 0
        temporary_fragment_list = []
        
        while True:
            fragment = file_content[fragment_count * fragment_size: (fragment_count + 1) * fragment_size]
            if not fragment:
                break
            fragment_count += 1
            
            while True:
                random_file_name = str(uuid4())
                if random_file_name not in fragment_list:
                    break
            
            # Stores this as a file in 'Data' directory in the current directory
            with open(f'Data/{random_file_name}', 'wb') as stream:
                stream.write(fragment)
            
            temporary_fragment_list.append(random_file_name)
            fragment_list.append(random_file_name)
        
        fragment_file = '\n'.join(temporary_fragment_list)
        cipher = AES.new(key, AES.MODE_EAX)
        encrypted_fragment_file, tag = cipher.encrypt_and_digest(fragment_file.encode('utf-8'))
        encrypted_fragment_file = cipher.nonce + encrypted_fragment_file + tag
        
        return encrypted_fragment_file
        # encrypted_fragment_file = AES.new(key, AES.MODE_EAX).encrypt(fragment_file.encode('utf-8'))    
        

    
    def __encryptFile(self, file, key):
        
        with open(file.name, 'rb') as stream:
            file_data = stream.read()
        
        cipher = AES.new(key, AES.MODE_EAX)
        encrypted_data, tag = cipher.encrypt_and_digest(file_data)
        encrypted_data = cipher.nonce + encrypted_data + tag
        
        return file_data, encrypted_data
    
    
    
    def __decryptAndCombineFragment(self, fragment, key):
        
        dcipher = AES.new(key, AES.MODE_EAX, nonce = fragment[:16])
        decrypted_data = dcipher.decrypt_and_verify(fragment[16:-16], fragment[-16:])
        decrypted_data = decrypted_data.decode('utf-8')
        
        combined_file = b''
        
        for fragment in decrypted_data.split('\n'):
            with open(f'Data/{fragment}', 'rb') as stream:
                combined_file += stream.read()
        
        return combined_file
    
    
    
    def __decryptFragment(self, fragment, key):
            
        dcipher = AES.new(key, AES.MODE_EAX, nonce = fragment[:16])
        decrypted_data = dcipher.decrypt_and_verify(fragment[16:-16], fragment[-16:])
        decrypted_data = decrypted_data.decode('utf-8')
        decrypted_data = decrypted_data.split('\n')
        
        return decrypted_data
    
    
    
    def __decryptFile(self, file, key):
        
        cipher = AES.new(key, AES.MODE_EAX, nonce = file[:16])
        decrypted_data = cipher.decrypt_and_verify(file[16:-16], file[-16:])
        
        return decrypted_data
    
    
    
    def __hashText(self, text):
        
        return sha256(text.encode()).hexdigest()
    
    
    
    def __keyDerivationFunction(self, username, password, file_password):
        result = ""
        for index in range(len(username)):
            result += chr(ord(username[index]) ^ ord(password[index]) ^ ord(file_password[index]))
        # result = result[:len(result)//2] + result[len(result)//2:]
        
        result = self.__hashText(result)
        result = result[:32], result[32:]
        new_result = ""
        for index in range(32):
            new_result += chr(ord(result[0][index]) ^ ord(result[1][index]))
        
        return new_result
    
    
    
    def createAccount(self, credentials):
        
        if not self.__checkConnection():
            pass
            # return '0'
        
        username = credentials['username'].lower()
        password = credentials['password']
        if not username or not password:
            return '1'
        display_name = credentials['display_name']
        
        username_hash = self.__hashText(username)
        password_hash = self.__hashText(password)
        
        payload = {
            'username': username_hash, 
            'password': password_hash, 
            'display_name': display_name, 
            'type': 'regular', 
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
            return '2'
    
    
    
    def loginAccount(self, credentials):
        
        if not self.__checkConnection():
            pass
            # return '0'
            
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
        
        if not self.__checkConnection():
            pass
            # return '0'
        
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
    
    
    
    def updateDisplayName(self, display_name, username):
        
        if self.MongoDB.updateDisplayName(username, display_name):
            return True
        else:
            return False
    
    
    
    def uploadFile(self, file, file_password, fragment_size, credentials, file_list, consumed_storage, allowed_storage):
        
        if not self.__checkConnection():
            pass
            # return '0'
        
        username = credentials['username']
        password = credentials['password']
        
        file_password_hash = self.__hashText(file_password)
        
        if self.MongoDB.checkExistance(username):
            user = self.MongoDB.retrieveUser(username)
            
            if user['password'] == password:
                if user['status'] == 'suspended':
                    return '3'
                
                name = file.name.split('/')[-1]
                extension, name = name.split('.')[-1], '.'.join(name.split('.')[:-1])
                size = path.getsize(file.name)
                if consumed_storage + round((size / 1024) / 1024, 3) > allowed_storage:
                    return '4'
                file_password_hash = self.__hashText(file_password)
                key = self.__keyDerivationFunction(username, password, file_password_hash)
                key_hash = self.__hashText(key)
                
                
                file_details = {
                    'name': name, 
                    'extension': extension, 
                    'size': round((size / 1024) / 1024, 3), 
                    'file_password_hash': file_password_hash,
                    'key_hash': key_hash
                }
                
                
                plain_text, encrypted_file = self.__encryptFile(file, key.encode('utf-8'))
                
                encrypted_fragment_file = self.__fragmentAndEncrypt(encrypted_file, fragment_size, key.encode('utf-8'))
                
                fragment_hash = self.__hashText(str(encrypted_fragment_file))
                file_details['fragment_hash'] = fragment_hash
                date = str(datetime.now())
                formated_date = f'{date[:4]}.{date[5:7]}.{date[8:10]}'
                file_details['date'] = formated_date
                file_list.append(file_details)
                self.MongoDB.uploadFile(username, file_list, consumed_storage + round((size / 1024) / 1024, 3))
                
                return file_list, consumed_storage + round((size / 1024) / 1024, 3), encrypted_fragment_file                
                
            else:
                return '1'
        else:
            return '2'
    
    
    
    def openFile(self, file, file_password, credentials, current_file):
        
        if not self.__checkConnection():
            pass
            # return '0'
        
        username = credentials['username']
        password = credentials['password']
        file_password_hash = self.__hashText(file_password)
        file_hash = self.__hashText(str(file))
        
        if file_password_hash != current_file['file_password_hash']:
            return '1'
        
        if file_hash != current_file['fragment_hash']:
            return '2'
        
        key = self.__keyDerivationFunction(username, password, file_password_hash)
        key_hash = self.__hashText(key)
        if key_hash != current_file['key_hash']:
            return '1'
        
        decrypted_fragment_file = self.__decryptAndCombineFragment(file, key.encode('utf-8'))
        
        decrypted_file = self.__decryptFile(decrypted_fragment_file, key.encode('utf-8'))
        
        return decrypted_file
    
    
    
    def renameFile(self, new_name, credentials, file_list, index):
        
        file_list[index]['name'] = new_name
        
        self.MongoDB.renameFile(credentials, file_list)
        
        return file_list
        
        
        
    def deleteFile(self, fragment_file, file_password, credentials, file_list, index, consumed_storage):
        
        username = credentials['username']
        password = credentials['password']
        file_password_hash = self.__hashText(file_password)
        file_hash = self.__hashText(str(fragment_file))
        
        if file_password_hash != file_list[index]['file_password_hash']:
            return '1'
        
        if file_hash != file_list[index]['fragment_hash']:
            return '2'
        
        key = self.__keyDerivationFunction(username, password, file_password_hash)
        key_hash = self.__hashText(key)
        if key_hash != file_list[index]['key_hash']:
            return '1'
        
        decrypted_fragment = self.__decryptFragment(fragment_file, key.encode('utf-8'))
        for fragment in decrypted_fragment:
            path = f'Data/{fragment}'
            try:
                remove(path)
            except:
                pass
        
        consumed_storage -= file_list[index]['size']
        file_list.pop(index)
        self.MongoDB.deleteFile(username, file_list, consumed_storage)
        
        return file_list, consumed_storage





def initiate():
    
    interface = DataHandler()





if __name__ == '__main__':
    
    try:
        initiate()
    except Exception as error:
        pass