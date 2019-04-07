#!/usr/bin/env python3.6
from users import Users
from users import Credentials
import string
import random

def create_account(username,account,password):
    '''
    Function to create a new account
    '''
    new_account = Users(username,account,password)
    return new_account
    
# def create_password(password):
#     '''
#     function to create a password
#     '''
#     new_password = Credentials(password)
#     return new_password

def save_account(users):
    '''
    function to save users
    '''
    users.save_user()

# def save_password(password):
#     '''
#     function to save users
#     '''
#     password.save_password()

def del_user(users):
    '''
    Function to delete a user account
    '''
    users.delete_account()
    
# def del_password(password):
#     '''
#     Function to delete a user password
#     '''
#     users.delete_password()
    
def display_accounts():
    '''
    function that returns all saved accounts
    '''
    return Users.display_accounts()

# def display_passwords():
#     '''
#     function that returns all saved accounts
#     '''
#     return Credentials.display_passwords()

def main():
    print("Welcome to Password locker Version 1.0. What is your name?")
    
    user_name = input()
    print('\n')
    print(f"Hello {user_name}.Please follow the instructions below to proceed with creating a locker account.")
    print('\n')
    
    while True:
        print("Use these key words to continue : ca - create a new account, da -display all active accounts, ex -exit the password locker")
        
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
                print(f"New account with username {username} for the account {account} successfully created")
                save_account(create_account(username,account,password)) # saving the new user details created
                # save_password(create_password(password)) # saving the password
            
            elif password == 'random':
                def randomPassword(length):
                    letters = string.ascii_letters
                    return ''.join((random.choice(letters)) for i in range(length))
                password = randomPassword(8)
                print("Your password is ", randomPassword(8))
              
                    
                save_account(create_account(username,account,password)) # saving the new user details created
                # save_password(create_password(password)) # saving the password
                print('\n')
                print(f"New account with username {username} for the account {account} successfully created")
        
        elif key_word == 'da':
            if display_accounts():
                print("Here is a list of all your created accounts")
                print('\n')
                
                for user in display_accounts():
                    print(f"Username :{user.username}...Account :{user.account}...Password :{user.password}")

                    
                    print('\n')
            else:
                print('\n')
                print("You don't seem to have created any accounts yet")
        elif key_word ==  'ex':
            print("Thank You for choosing the Password locker.Byee..")
            break
            
    else:
        print
        ("Please use the specified keywords to access our services.")      
            
                    
                    
                    
        
        

if __name__ == "__main__":
    main()
    
    