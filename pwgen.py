# Password Encoder
# Author: j-l0
# A simple, offline password encoder.
# The purpose of the script is to assist in circumventing authentication attacks by 
# creating stronger passwords via encoding.

#Modules
import subprocess
import base64
import string
import pyperclip3

# #User input of plaintext password
print('Please temporarily disable Wi-Fi or network connections. \nTip: Using a password atleast 12 characters in length is recommended.')
strpw = input('Please enter your plaintext password: ')

#Encoding plaintext > string > bytes
bytepw = strpw.encode('utf-8')
encpw = base64.b64encode(bytepw)
pyperclip3.copy(encpw)

#Copied to clipboard
print('Copied to clipboard.')

#exit program
input('Press enter to close.')
