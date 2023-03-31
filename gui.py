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
				try:
								if event == "Encrypt":
												key = cf.keygen()
												cf.key_write(key)
												key = cf.key_load()
												file_path = values[0]
												file_type = file_path.split(".")[1]
												file_type = "." + file_type

												if file_type not in [".csv", ".txt"]:
																raise ValueError("Invalid file type.")

												cf.encrypt(key,file_path,file_type)


								elif event == "Decrypt":
												key = cf.key_load()
												file_path = values[0]
												file_type = file_path.split(".")[1]
												file_type = "." + file_type

												if file_type not in [".csv", ".txt"]:
																raise ValueError("Invalid file type.")

												cf.decrypt(key,file_path,file_type)

								elif event == sg.WIN_CLOSED:
												break

				except Exception as e:
								sg.PopupError(f"An error occurred: {str(e)}")

window.close()




