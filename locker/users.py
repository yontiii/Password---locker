class Users:
    """
    Class that generate new instances of users
    """
    accounts_list = []# empty users list where all accounts created will be stored
    
    def __init__(self,username,account):
         """
         Args:
         username: new User username
         account: new User account
         """
         self.username = username
         self.account = account
         
    def save_user(self):
        Users.accounts_list.append(self)
    
class Credentials:
    """
    Class that generates new instances of passwords
     """
    def __init__(self,password):
        self.password = password
    
    def save_password(self):
        Users.accounts_list.append(self)
   