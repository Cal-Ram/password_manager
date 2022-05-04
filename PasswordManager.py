# This will be a program that records, encrypts, stores, and relays usernames and passwords from various websites
from tkinter import *

allowed_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!?<>@$£^()"
# getting the password from the user
website = input("Which website is this password being used for?")
username = input("What is your username for the website?")
password = input("What is the password for the website?")

def isvalid(password):
    for char in password:
        if char not in allowed_chars:
            print("The only available characters are the common alphabet, numbers, and !?<>@$£^()")
# Encrypting the password
def encrypt(password):
    encrypted = ""
    for char in password:
        new = chr(ord(char) + 3)
        encrypted += new
    return encrypted
# storing the password
def storing_data():
    file = open("passwordmanager.csv", "w")

# reading the password

# decrypting the password
def decrypt(password):
    decrypted = ""
    for char in password:
        new = chr(ord(char) - 3)
        decrypted += new
    return decrypted
# user interface for the application

window = Tk()
window.title("Password Manager")
window.geometry("500x600")
window.mainloop()
