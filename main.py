from cryptography.fernet import Fernet

# Create a key
key = Fernet.generate_key()

with open("mykey.key","wb") as mykey:
				mykey.write(key)

#Load key

with open("mykey.key","rb") as mykey:
				key = mykey.read()





