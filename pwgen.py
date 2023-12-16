import bcrypt 
import hashlib
import base64
import os
import sys
import maskpass
import pyperclip3 as pc


def quit():
     sys.exit(0)

def hashed():
    password = maskpass.askpass(mask="") 
    bytes = password.encode('utf-8')     # converting password to array of bytes 
    salt = bcrypt.gensalt()     # generating the salt 
    hash = bcrypt.hashpw(bytes, salt)     # Hashing the password 
    pc.copy(hash)

def base64en():
    password = maskpass.askpass(mask="") 
    password_bytes = password.encode('utf-8')
    # Encode the password in Base64
    encoded_password = base64.b64encode(password_bytes)
    pc.copy(encoded_password)

def base32en():
    password = maskpass.askpass(mask="") 
    password_bytes = password.encode('utf-8')
    # Encode the password in Base64
    encoded_password = base64.b32encode(password_bytes)
    pc.copy(encoded_password)

def base16en():
    password = maskpass.askpass(mask="") 
    password_bytes = password.encode('utf-8')
    # Encode the password in Base64
    encoded_password = base64.b16encode(password_bytes)
    pc.copy(encoded_password)



def menu():
    print('----------------------------------------------------------')
    print('                 Python Password Encryption Tool          ')
    print('----------------------------------------------------------')

    print('1) Select Bcrypt Encryption')
    print('2) Select Base64 Encoding')
    print('3) Select Base32 Encoding')
    print('4) Select Base16 Encoding')
    print('5) exit')

def main():
    while True:
        menu()

        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Invalid input. Please enter a number 1 through 5.")
            continue
        if choice == 1:
            hashed()
        elif choice == 2:
            base64en()
        elif choice == 3:
            base32en()
        elif choice == 4:
            base16en()
        elif choice == 5:
            quit()

            
if __name__ == "__main__": 
	main()
    

