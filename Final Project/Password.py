import re
import hashlib
SpecialSym =['$', '@', '#', '%']

def validate():
    while True:
        password = input("Enter a password: ")
        if len(password) < 8:
            print("Password must be 8 characters")
        elif re.search('[0-9]',password) is None:
            print("Password must contain a number")
        elif re.search('[A-Z]',password) is None:
            print("Password must contain a capital letter")
        elif re.search('[SpecialSym]',password) is None:
            print("Password must contain a symbol")
        else:
            print("Password created")
        user_entered_password = password
        salt = "5gz"
        db_password = user_entered_password+salt
        h = hashlib.md5(db_password.encode())
        print(h.hexdigest())
        break
validate()

## I couldn't find a way to decrypt a hash online. Most articles that came up said that hashing is one way. I'm not sure how to decrypt the hash.
