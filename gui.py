import cryptographic_functions as cf
import PySimpleGUI as sg
import csv, os

working_directory = os.getcwd()
file_types = (
    ("All CSV and TXT Files","*.csv *.txt"),
)


label = sg.Text("Encrypt or Decrypt a File")
input_box =\
				sg.Text("Choose a file"),\
				sg.InputText(),\
				sg.FileBrowse(initial_folder=working_directory, file_types=file_types)
buttons = sg.Button("Encrypt"), sg.Button("Decrypt")

window = sg.Window("Cryptography App",
																			layout=[[label],
																										[input_box],
																										[buttons]],
																			font=("Helvetica",14))

while True:
				event, values = window.Read()
				match event:
								case "Encrypt":
												key = cf.keygen()
												cf.key_write(key)
												key = cf.key_load()
												value = values[0]
												file_type = value.split(".")[1]
												file_type = "." + file_type
												cf.encrypt(key,value,file_type)
								case "Decrypt":
												key = cf.key_load()
												value = values[0]
												file_type = value.split(".")[1]
												file_type = "." + file_type
												cf.decrypt(key,value,file_type)

								case sg.WIN_CLOSED:
												break

window.close()




