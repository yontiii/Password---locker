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
        '''
        function  that adds new users to the contacts list
        '''   
        
    def delete_user(self):
        '''
        method that deletes user accounts
        '''
        Users.accounts_list.remove(self) 
        
    def save_user(self):
        Users.accounts_list.append(self)
    
    # @classmethod
    # def display_contacts(cls):
    #     return Users.accounts_list
    
class Credentials:
    """
    Class that generates new instances of passwords
     """
    def __init__(self,password):
        self.password = password
    
    '''
    function to add passwords to the accounts list
    '''
    def save_password(self):
        Users.accounts_list.append(self)
    '''
    Function to delete passwords from the accounts list
    '''
    def delete_password(self):
        Users.accounts_list.remove(self)
        

  
   