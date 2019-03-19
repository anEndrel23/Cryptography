"""
cryptography.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

yaboi = 7

while yaboi != 6:
    prompt = str(input("Enter e to encrypt, d to decrypt, or q to quit: "))
    for i in prompt:
            if i == 'e':
                msg = input('Message: ')
                key = input('Key: ')
                gg = ''
                if len(msg) > len(key):
                    while True:
                        gg += key
                        if len(gg) >= len(msg):
                            break
                em = [associations.find(x) for x in msg]
                ek = [associations.find(y) for y in gg]
                mm = [em + ek for em, ek in zip(em, ek)]
                outpt = ''.join(associations[i % len(associations)] for i in mm)
                print(outpt)
            elif i == "d":
                msg = input('Message: ')
                key = input('Key: ')
                gg = ''
                if len(msg) > len(key):
                    while True:
                        gg += key
                        if len(gg) >= len(msg):
                            break
                em = [associations.find(x) for x in msg]
                ek = [associations.find(y) for y in gg]
                mm = [em - ek for em, ek in zip(em, ek)]
                outpt = ''.join(associations[i % len(associations)] for i in mm)
                print(outpt)
            elif i == "q":
                print("Goodbye!")
                return
            else:
                print("Did not understand command, try again.")