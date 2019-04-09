#!/usr/bin/env python3.6
from users import Users
from users import Credentials
from prettytable import PrettyTable 
import colored
from colored import stylize
import string
import random

def create_account(username,account,password):
    '''
    Function to create a new account
    '''
    new_account = Users(username,account,password)
    return new_account
    
def create_credentials(magicword,account,email):
    '''
    function to create a credential
    '''
    new_credentials = Credentials(magicword,account,email)
    return new_credentials

def save_account(users):
    '''
    function to save users
    '''
    users.save_user()

def save_credentials(credentials):
    '''
    function to save credentials
    '''
    credentials.save_credential()

def del_user(users):
    '''
    Function to delete a user account
    '''
    users.delete_account()
    
def del_credentials(credentials):
    '''
    Function to delete a user credentials
    '''
    credentials.delete_credential()
    
def display_accounts():
    '''
    function that returns all saved accounts
    '''
    return Users.display_accounts()

def display_credentials():
    '''
    function that returns all saved credentials
    '''
    return Credentials.display_credentials()

def find_by_account(account):
    '''
    function to return an account searched for by username
    '''
    return Users.find_by_account(account)

def main():
    print(stylize("Welcome to Password locker Version 1.0. What is your name?",colored.fg("blue")))
    
    user_name = input()
    print('\n')
    print(f"Hello {user_name}.Please follow the instructions below to proceed with creating a locker account.")
    print('\n')
    
    while True:
        print(stylize("Use these key words to continue : ca - create a new account, da -display all active accounts, cc- to create a credential for your account, dc - to display credentials ,del - to delete an  account, ex -exit the password locker",colored.fg("green")))
        print("\n")
        
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
            
            password = input("Enter Password type :  ").lower()

            if password == 'own':
                print("Enter Password")
                password = input()
                print("confirm password")
                confirmpassword = input()
                if password == confirmpassword:
                    print(f"New account with username {username} for the account {account} successfully created")
                    save_account(create_account(username,account,password)) # saving the new user details created
                # save_password(create_password(password)) # saving the password
                else:
                      print("Your passwords don't match.")
                
            elif password == 'random':
                def randomPassword(length):
                    letters = string.ascii_letters
                    return ''.join((random.choice(letters)) for i in range(length))
                password = randomPassword(8)
                print("Your password is ", randomPassword(8))
              
                    
                save_account(create_account(username,account,password)) # saving the new user details created
                # save_password(create_password(password)) # saving the password
                print('\n')
                print(stylize(f"New account with username {username} for the account {account} successfully created",colored.fg("green")))
        
        elif key_word == 'da':
            if display_accounts():
                print("Here is a list of all your created accounts")
                print('\n')
                
                for user in display_accounts():
                    table = PrettyTable()
                    table.field_names = ["UserName","Account","Password"]
                    table.add_row([user.username,user.account,user.password])
                    print(table)

                    
                    print('\n')
            else:
                print('\n')
                print(stylize("You don't seem to have created any accounts yet",colored.fg("red")))
                
                
        elif key_word == 'cc':
            print("Creating a Credential for your account lets you save important details of the password")
            print("\n")
            print("-" *10)
            print("Enter a magicword that will help you remember your passwords easily")
            magicword = input()
            print("\n")
            print("Enter the name of the account you are creating the credentials")
            account = input()
            print("Enter your email please")
            email = input()
            
            save_credentials(create_credentials(magicword,account,email))
            print(stylize(f"New Credentials for the account {account} successfully created",colored.fg("green")))
            
        elif key_word == 'dc':
            print("Here are all your credentials")
            print("\n")
            
            for words in display_credentials():
                c_table = PrettyTable()
                c_table.field_names=["MagicWord","Account","Email"]
                c_table.add_row([words.magicword,words.account,words.email])
                print(c_table)
                
        # elif key_word == 'del':
        #     print("Once an Account is deleted, it can't be undone")
        #     confirm = input("Enter name of the account you wish to delete ")
        #     find_by_account()
        #     print(f"{member.password},{member.account},{member.username}")
            
            
            
        elif key_word ==  'ex':
            print(stylize("Thank You for choosing the Password locker.Byee..",colored.fg("yellow")))
            break
            
    else:
        print
        ("Please use the specified keywords to access our services.")      
            
                    
                    
                    
        
        

if __name__ == "__main__":
    main()
    
    