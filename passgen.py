#!/usr/bin/python3

# Secure password generator 

import random
import string

# Generate random password strings of given length

def generate_password(length):
    password = ''
    for i in range(length):
        password += random.choice(string.ascii_letters + string.digits)
    return password

# Call the function
print("Enter a desired length for your password:")
len = int(input())
newpass = generate_password(len)
print(newpass)
