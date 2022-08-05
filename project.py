from password_generator import generatePassword
from password_validator import checkRequirementsMeet, checkPasswordStrength
from usercode_generator import generate_code
from email_verification import checkEmailFormat
from send_confirm_email import sendEmail

# SQL Connector

from argparse import _MutuallyExclusiveGroup
from multiprocessing.sharedctypes import Value
from sre_compile import isstring
from sys import excepthook
import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='sqluser',
    password='password',
    database='user'
)
mycursor = mydb.cursor()

class User:
    def __init__(self, name, surname, password, email, code):
        self.name = name
        self.surname = surname
        self.password = password
        self.email = email
        self.code = code

    def userForm():
        print(f"Fill all the fields to create an account")
        name = input(f'Name: ')
        surname = input(f"Surname: ")
        email = checkEmailValid()
        code = setCode()
        password = checkPasswordValid()
        print(f"Account informations summary\n")
        print(
            f"Name: {name}\nSurname: {surname}\nEmail: {email}\nUser identifier: {code}\n"
        )
        create = input(f"Press enter to create account ")
        if create == '':
            mycursor.execute(
                "INSERT INTO Account(name, surname, email, code, password) VALUES ( %s, %s, %s, %s, %s)", (
                    name, surname, email, code, password)
            )
            print(
                f"Account have been created successfully. We will send you confirmation to your email.")
            sendEmail(email)

def setCode():
    code = generate_code()
    mycursor.execute(
        "SELECT code FROM Account WHERE code = %s;", (code, )
    )
    while len(mycursor.fetchall()) > 0:
        code = setCode()
    if len(mycursor.fetchall()) == 0:
        return code

# email verification

def checkEmailValid():
    email = input(f"Email: ")
    while checkEmailFormat(email) == False:
        email = input(
            f"Email does not meet requirements please try again.\nEmail: "
        )
    if checkEmailFormat(email) == True:
        if checkEmailAvailable(email) == True:
            return email

def checkEmailAvailable(email):
    mycursor.execute(
        "SELECT email FROM Account WHERE email = %s;", (email, )
    )
    while len(mycursor.fetchall()) > 0:
        email = input(
            f"Email already registered. Please choose another email address\nEmail: "
        )
        checkEmailValid(email)
    if len(mycursor.fetchall()) == 0:
        return True

# password verification

def checkPasswordValid():
    print(f"Do you want your password to be generated automatically?")
    generate = input(f"1) Yes 2) No, I want to set it manually\n")
    while str(generate) != '1' and str(generate) != '2':
        generate = input(f"Please choose option 1 or 2\n")
    if str(generate) == '2':
        password = input(f"Password: ")
        while checkRequirementsMeet(password) == False:
            password = input(
                f"Password does not meet requirements. Please try again\nPassword: "
            )
        if checkRequirementsMeet(password) == True:
            if confirmPassword(password) == True:
                strength = checkPasswordStrength(password)
                print(f"Password strength: {strength}")
                return password
    elif str(generate) == '1':
        password = generatePassword()
        print(f"Your password is set for {password}")
        return password

def confirmPassword(password):
    confirm_try = input(f"Confirm password: ")
    while confirm_try != password:
        confirm_try = input(
            'There is difference between passwords.Try again\nConfirm password: ')
    if confirm_try == password:
        return True


def main():
    start = User
    start.userForm()


if __name__ == "__main__":
    main()


