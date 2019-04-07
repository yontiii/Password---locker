class Users:
    """
    Class that generate new instances of users
    """
    accounts_list = []# empty users list where all accounts created will be stored
    
    def __init__(self,username,account,password):
        """
        Args:
        username: new User username
        account: new User account
        """
        self.username = username
        self.account = account
        self.password = password
        '''
        function  that adds new users to the accounts list
        '''   
    def save_user(self):
        Users.accounts_list.append(self)
        
    def delete_account(self):
        Users.accounts_list.remove(self)
        '''
        method that removes an account from the accounts list
        '''
    
    @classmethod
    def display_accounts(cls):
        '''
        method that returns the accounts list
        '''
        return cls.accounts_list
    
    
class Credentials:
    """
    Class that enables users to key in their credentials to help them remember their passwords easily
     """
    def __init__(self,magicword,account,email):
        '''
        initialized the class with three arguments
        '''
        self.magicword = magicword
        self.account = account
        self.email =email
    
    Credentials_list = []
    '''
    list that holds every credential made
    '''
    
    def save_credential(self):
        Credentials.Credentials_list.append(self)
        
    def delete_credential(self):
        Credentials.Credentials_list.remove(self)
        '''
        method that removes a credential from the credentials list
        '''
    @classmethod
    def display_credentials(cls):
        '''
        method that returns the contact list
        '''
        return cls.Credentials_list
    

  
   