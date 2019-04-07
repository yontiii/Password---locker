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
        self.password = password
        self.confirmpassword = confirmpassword
        '''
        function  that adds new users to the accounts list
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
    Class that enables users to key in their credentials to help them remember their passwords easily
     """
    

  
   