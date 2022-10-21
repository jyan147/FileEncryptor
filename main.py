#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : main.py
# Author             : jyan147
# Date created       : 21 Oct 2022

from email.message import Message
from fileinput import filename
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showerror, showinfo
from cryptography.fernet import Fernet

#window
window = tk.Tk()
window.title('File Cryptor')
window.resizable(False,False)
window.eval('tk::PlaceWindow . center')
window.geometry('650x300')

with open('secret.key', 'rb') as mykey: #select your key here
    key = mykey.read()
    f = Fernet(key)


def select_file():
    try:
        filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
        )
            
        filename = fd.askopenfilename(
        title = 'Select file to encrypt',
        initialdir= '/',
        filetypes = filetypes
        )

        if not filename or filename is None:
            showinfo(
            title= "Info",
            message = "No file selected."
            )
        else :
            with open(filename, 'rb') as original_file:
                original = original_file.read()

            encrypted = f.encrypt(original) #encryption
            with open('file.enc', 'wb') as encrypted_file:
                encrypted_file.write(encrypted)
            showinfo(
            title= "Succes",
            message= "Your file has been encrypted successfully." + filename
            )
            
    except IOError:
        print("File does not exist.")
        showerror(
            title= "Error",
            message= "An error has occurred"
        )
    finally:
        pass


#decryption
def Decrypt_file():
    with open('file.enc', 'rb') as encrypted_file:
        encrypted = encrypted_file.read()
    decrypted = f.decrypt(encrypted) #decryption
    with open('file.dec', 'wb') as decrypted_file: #create and write decrypted file
       decrypted_file.write(decrypted)

    showinfo(
        title= "Succes",
        message= "Your file has been decrypted successfully."
    )


if __name__ == "__main__":
    #button for selection
    Button_Select = ttk.Button(
    window,
    text = 'Select',
    command = select_file
    )

    Button_Decrypt = ttk.Button(
        window,
        text = 'Decrypt',
        command= Decrypt_file
    )


    #button
    Button_Select.pack(expand=True)
    Button_Decrypt.pack(expand=True)

    #display window
    window.mainloop()
