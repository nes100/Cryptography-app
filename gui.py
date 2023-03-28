import cryptographic_functions as cf
import PySimpleGUI as sg
import csv, os

working_directory = os.getcwd()
file_types = (
    ("All CSV and TXT Files","*.csv *txt"),
)

label = sg.Text("Encrypt or Decrypt a File")
encrypt =\
				sg.Text("Enter the path of the file you want to encrypt"),\
				sg.InputText(),\
				sg.FileBrowse(initial_folder=working_directory, file_types=file_types),\
				sg.Button("Encrypt")
decrypt =\
				sg.Text("Enter the path of the file you want to decrypt"),\
				sg.InputText(),\
				sg.FileBrowse(initial_folder=working_directory, file_types=file_types),\
				sg.Button("Decrypt")

window = sg.Window("Cryptography App",
																			layout=[[label],
																										[encrypt],
																									 [decrypt]],
																			font=("Helvetica",14))

window.read()

window.close()