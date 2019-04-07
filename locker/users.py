class Users:
    """
    Class that generate new instances of users
    """
    accounts_list = []# empty users list where all accounts created will be stored
    
    def __init__(self,username,account,password,confirmpassword):
        """
        Args:
        username: new User username
        account: new User account
        """
        self.username = username
        self.account = account
        self.account = account
        self.account = account
        '''
        function  that adds new users to the contacts list
        '''   
        
  
    def save_user(self):
        Users.accounts_list.append(self)
        
    def delete_account(self):
        Users.accounts_list.remove(self)
    
    @classmethod
    def display_accounts(cls):
        '''
        method that returns the contact list
        '''
        return cls.accounts_list
    
    
class Credentials:
    """
    Class that generates new instances of passwords
     """
     
    passwords_list = []
     
    def __init__(self,password):
        self.password = password
    
    '''
    function to add passwords to the accounts list
    '''
    def save_password(self):
        Credentials.passwords_list.append(self)
    '''
    Function to delete passwords from the accounts list
    '''
    
    def delete_password(self):
        Credentials.passwords_list.remove(self)
        
    @classmethod
    def display_passwords(cls):
        '''
        method that returns the contact list
        '''
        return cls.passwords_list

  
   