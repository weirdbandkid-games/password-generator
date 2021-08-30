import random

chars = "abcdefghijklmopqrstuvwxyzABCDEFGHIJKLMOPQRSTUVWXYZ1234567890&;:/\|{}[]-=_+^%$#!@*"

while 1:
    password_len = int(input("What will be the lenght of the password? "))
    password_count = int(input("How many passwords will you like? "))
    for x in range(0,password_count):
        # print(x)
        password = ""
        for x in range(0,password_len):
            password_char = random.choice(chars)
            # print(password_char)
            password = password + password_char
        print("Here is your password: \n", password)

# © Hunter Fleming 2021
