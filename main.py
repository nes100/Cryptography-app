from cryptography.fernet import Fernet

# Create a key
key = Fernet.generate_key()

with open("mykey.key","wb") as mykey:
				mykey.write(key)

#Load key
with open("mykey.key","rb") as mykey:
				key = mykey.read()

#Initialize Fernet object
f = Fernet(key)

#Open data file in plaintext
with open("data.csv","rb") as file:
				data = file.read()

# Encrypt data and store as encrypted
encrypted = f.encrypt(data)

#Write ecrypted data into new csv file
with open("encrypted_data","wb") as file:
				file.write(encrypted)





