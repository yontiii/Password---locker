#!/usr/bin/env python3.6
from users import Users
from users import Credentials
import string
import random

def create_account(username,account):
    '''
    Function to create a new account
    '''
    new_account = Users(username,account)
    return new_account
    
def create_password(password):
    '''
    function to create a password
    '''
    new_password = Credentials(password)
    return new_password

def save_account(users):
    '''
    function to save users
    '''
    users.save_user()

def save_password(password):
    '''
    function to save users
    '''
    password.save_password()

def del_user(users):
    '''
    Function to delete a user account
    '''
    users.delete_account()
    
def del_password(password):
    '''
    Function to delete a user password
    '''
    users.delete_password()
    
def display_contacts():
    '''
    function that returns all saved accounts
    '''
    return Users.display_accounts()

def main():
    print("Welcome to Password locker Version 1.0.Please tell Us your  name")
    
    user_name = input()
    
    print(f"Hello {user_name}.Please follow the instructions below to proceed with creating a locker account for your passwords")
    print('\n')
    
    while True:
        print("Use these key words to continue : ca - create a new account, da -display all active accounts, ex -exit the password  locker")
        
        key_word = input().lower()
        
        if key_word == 'ca':
            print("New Account")
            print("*" * 8)
            
            print("Account Username ***")
            username = input()
            
            print("Account name")
            account = input()
            
            print("\n")
            print("Its now time to create a password.To create your own password type own and to get an automatic one type random")
            
            password_type = input("Enter Password type :  ").lower()

            if password_type == 'own':
                print("Enter Password")
                password = input()
            
            elif password_type == 'random':
                def randomPassword(length):
                    letters = string.ascii_letters
                    return ''.join((random.choice(letters)) for i in range(length))
                print("Your password is ", randomPassword(8))
                else:
                    print("Please make a valid choice")
                   save_account(create_account(username,account)) # saving the new user details created 
                    
                    
                    
        
        

if __name__ == "__main__":
    main()
    
    