#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : keygen.py
# Author             : jyan147
# Date created       : 21 Oct 2022

from email.mime import base
from cryptography.fernet import Fernet
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

#Generate a key and save it into a file
def gen_key():
    key = Fernet.generate_key()
    print(key)
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    key_file.close()

#Loads the key from the current directory named "secret.key"
def load_key():
    return open("secret.key", "rb").read()

def Encrypt():
    password_provided = "yourpassword" #type your pass here
    password = password_provided.encode()

    salt = b'|\xdb\xfbG\xa4\xbb\xa9m-4\xf2Y\x04\xc1\xa5#' #us.urandom(16)

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt= salt,
        iterations= 100000,
        backend=default_backend()
    )

    key = base64.urlsafe_b64encode(kdf.derive(password))
    print(key)

if __name__ == "__main__":
    Encrypt()
