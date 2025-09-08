#symmetric encryption using fernet
from cryptography.fernet import Fernet

def write_key():
   # Generates a key and save it into a file
   key = Fernet.generate_key() #genrates a fresh fernet key
   with open("key.key", "wb") as key_file:
        key_file.write(key )

#create a function to load the key for us since the key is unique and will not be generate deach time anything is encrypted
def load_key():
    # Loads the key from the current directory named `key.key`
    return open("key.key", "rb").read()   

#generate and write a new key
write_key()

#load the previously generated key
key = load_key()

message = "hello world"
#encode the message
encoded_message = message.encode()
#encode method encodes string using utf-8 encoding
#initialize the fernet class
f = Fernet(key)

#encrypt the message
encrypted = f.encrypt(encoded_message)

print(encrypted)  #prints the encrypted message

#decrypt the message
decrypted = f.decrypt(encrypted)
print(decrypted)  #prints the decrypted message






