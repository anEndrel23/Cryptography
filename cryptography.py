"""
cryptography.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

prompt = str(input("Enter e to encrypt, d to decrypt, or q to quit: "))

for i in prompt:
    if i == "e":
        msg = input("Message: ")
        msg = text.split(msg)
        key = input("Key: ")
        key = text.split(key)
        for x in msg:
            print(associations.find(x))
        print(associations.find(y) for y in key)
    elif i == "d":
        dmsg = input("Message: ")
        dkey = input("Key: ")