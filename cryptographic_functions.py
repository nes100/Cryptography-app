from cryptography.fernet import Fernet

def keygen():
				"""
				Function to generate an encryption key
				:return: key
				"""
				key = Fernet.generate_key()
				return key
def key_write(key):
				"""
				Function that writes encryption key into a file
				:param key:
				:return: mykey.key file
				"""
				with open("mykey.key","wb") as mykey:
								mykey.write(key)

def key_load():
				"""
				Function to load encryption key from a file
				:return: key
				"""
				with open("mykey.key","rb") as mykey:
								key = mykey.read()
								return key


def encrypt(key,file,file_type):
				"""
				Function to encrypt a file
				:param key: key
				:param file: file you want to encrypt
				:return:
				"""
				f = Fernet(key)

				with open(file,"rb") as file:
								data = file.read()

				encrypted = f.encrypt(data)

				with open("encrypted_data" + file_type,"wb") as encrypted_file:
								encrypted_file.write(encrypted)

def decrypt(key,encrypted_data,file_type):
				"""
				Function that decrypts an encrypted file
				:param key: key
				:param encrypted_data:
				:return:
				"""
				f = Fernet(key)

				with open(encrypted_data,"rb") as encrypted_file:
								encrypted = encrypted_file.read()

				decrypted = f.decrypt(encrypted)

				with open("decrypted_data" + file_type,"wb") as decrypted_file:
								decrypted_file.write(decrypted)



