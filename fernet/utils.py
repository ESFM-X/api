from cryptography.fernet import Fernet

path = "../private/fernet.key" if __name__ == "__main__" else "private/fernet.key"

with open(path, "rb") as f:
    byte = f.read(1)
    key = b''
    while byte != b"":
        # Do stuff with byte.
        key += byte
        byte = f.read(1)
    
f = Fernet(key)

def encrypt(text):
   
    return f.encrypt(text.encode())

def decrypt(bytes):
    return str(f.decrypt(bytes), 'UTF-8')
