"""
cryptography.py
Author: Andrew
Credit: Stack overflow, matt

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

itsyaboi = 7



while itsyaboi != 6:
    prompt = str(input("Enter e to encrypt, d to decrypt, or q to quit: "))
    if prompt == "q":
        itsyaboi = 6
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
                eadd = [em + ek for em, ek in zip(em, ek)]
                outpt = ''.join(associations[i % len(associations)] for i in eadd)
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
                eadd = [em - ek for em, ek in zip(em, ek)]
                outpt = ''.join(associations[i % len(associations)] for i in eadd)
                print(outpt)
            elif i == "q":
                break
            else:
                print("Did not understand command, try again.")
                
print("Goodbye!")