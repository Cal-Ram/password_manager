# This will be a program that records, encrypts, stores, and relays usernames and passwords from various websites
from tkinter import *
import csv

allowed_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!?<>@$£^()"
# getting the password from the user
website = ""
username = ""
password = ""
can_continue = True
def isvalid(password):
    for char in password:
        if char not in allowed_chars:
            print("The only available characters are the common alphabet, numbers, and !?<>@$£^()")
            can_continue = False
# Encrypting the password
def encrypt(password):
    encrypted = ""
    for char in password:
        new = chr(ord(char) + 3)
        encrypted += new
    return encrypted
# storing the password
def storing_data(website, username, password):
    file = open("passwordmanager.csv", "a")
    writer = csv.writer(file)
    writer.writerow([website, username, password])
    file.close()

def enter_password(website, username, password):
    can_continue = True
    isvalid(password)
    if can_continue is True:
        encrypt(password)
        storing_data(website, username, password)
# reading the password
def read_password():
    file = open("passwordmanager.csv", "r")
    csv_reader = csv.reader(file, delimiter=",") # perhaps needs to be DictReader
    for row in csv:
        details = {"Website": row[1], "Username": row[2], "Password": row[3]}
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

# 3 input fields
website_input = Entry(window, textvariable=website)
website_input.grid(row=1, column=0, columnspan=2)
username_input = Entry(window, textvariable=username)
username_input.grid(row=1, column=4, columnspan=2)
password_input = Entry(window, textvariable=password)
password_input.grid(row=1, column=8, columnspan=2)
# button to add password
add_password = Button(window, text="Add Password", command=enter_password(website, username, password))
add_password.grid(row=3, column=2, columnspan=4)
# the current websites should be able to be viewed and then selected
# button to chose website to get password




window.mainloop()
