import cryptographic_functions as cf

key = cf.keygen()

cf.key_write(key)

key = cf.key_load()

cf.encrypt(key,"data.csv")

cf.decrypt(key,"encrypted_data")







