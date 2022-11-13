import os
from Crypto.PublicKey import RSA
import base64
def gen_key():
    if not  os.path.exists('src/key/private.pem'):
        key = RSA.generate(2048)
        private_key = key.export_key()
        public_key = key.publickey().export_key()
        with open('src/key/private.pem', 'wb') as f:
            f.write(private_key)
        with open('src/key/public.pem', 'wb') as f:
            f.write(public_key)
def get_base64_public_key():
    with open('src/key/public.pem', 'rb') as f:
        public = f.read()
    print(base64.b64encode(public))

def get_base64_private_key():
    with open('src/key/private.pem', 'rb') as f:
        public = f.read()
    print(base64.b64encode(public))
if __name__== '__main__':
    gen_key()
    get_base64_private_key()