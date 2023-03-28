import cryptographic_functions as cf
import PySimpleGUI as sg
import csv, os

label = sg.Text("Encrypt or Decrypt a File")
input_box1 = sg.Text("Enter the path of the file you want to encrypt"), sg.InputText("FILE_PATH"), \
				sg.Button("Browse"), sg.Button("Encrypt")
input_box2 = sg.Text("Enter the path of the file you want to decrypt"), sg.InputText(), \
				sg.Button("Browse"), sg.Button("Decrypt")

window = sg.Window("Cryptography App",
																			layout=[[label],
																										[input_box1],
																											[input_box2]],
																			font=("Helvetica",14))

window.read()

window.close()