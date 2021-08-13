import random
import tkinter
import string
#title = input("name the title")# I will change this to a tkinter entry field
# the entry fields will also choose the min and max characters
# I will use a mix of checkbuttons and entry fields for allowed_characters
title = "bob"


def random_password(min_characters, max_characters, allowed_characters):
    password = ""
    for char in range(min_characters, max_characters):    
        password += random.choice(allowed_characters)
    return password

data = title + " " + random_password()

file = open("passwords.txt", "w")
file.write(data)
file.close()

file = open("passwords.txt", "r")
print(file.readlines())