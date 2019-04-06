import unittest
import users  

class TestUsers(unittest.TestCase):
    '''
    TestCase that defines test cases for the user and credential class behaviours
    '''
    def setUp(self):
        '''
        setUp method to run before each cases
        '''
        self.new_account = users.Users("John","Facebook")
        self.new_password = users.Credentials("jklmn25")
        
    def tearDown(self):
        '''
        tearDown method that cleans up after each testCase is done
        '''
        users.Users.accounts_list = []
        users.Credentials.passwords_list =[]
    
    def test_init(self):
        self.assertEqual(self.new_account.username,"John")
        self.assertEqual(self.new_account.account,"Facebook")
        self.assertEqual(self.new_password.password,"jklmn25")
    
    
        
        
    def test_save_user(self):
         '''
         To test if the account created is stored in the users list
         '''
         
         self.new_account.save_user()   
         self.assertEqual(len(users.Users.accounts_list),1)
         
    def test_save_password(self):
        ''''
        To test if the password is being saved in the passwords list
        '''
        self.new_password.save_password()
        self.assertEqual(len(users.Credentials.passwords_list),1)
    
    def test_save_multiple_accounts(self):
        '''
        This is to check whether multiple users can create multiple accounts
        '''
        self.new_account.save_user()
        
        
        test_user = users.Users("test","account")
       
        test_user.save_user()
       
        self.assertEqual(len(users.Users.accounts_list),2)
       
        
    def test_save_multiple_passwords(self):
        '''
        This was a test to check whether multiple passwords can be created
        '''
        self.new_password.save_password()
        test_password = users.Credentials("abcdefk1")
        test_password.save_password()
        self.assertEqual(len(users.Credentials.passwords_list),2)
    
    def test_delete_account(self):
        '''
        test_delete account to see if we can remove an account from the list
        '''
        self.new_account.save_user()
        test_account = users.Users("test","gmail")
        test_account.save_user()
        self.new_account.delete_account()
        self.assertEqual(len(users.Users.accounts_list),1)
        
    def test_delete_password(self):
        '''
        test_delete password to see if we can remove a password from the list
        '''
        self.new_password.save_password()
        test_password = users.Credentials("klcv8yio")
        test_password.save_password()
        self.new_password.delete_password()
        self.assertEqual(len(users.Credentials.passwords_list),1)
        
        
    def test_display_accounts(self):
        '''
        Method that returns a list of all saved accounts
        ''' 
        self.assertEqual(users.Users.display_accounts(),users.Users.accounts_list)
        
        
    def test_display_passwords(self):
        '''
        Method that returns a list of all saved accounts
        ''' 
        self.assertEqual(users.Credentials.display_passwords(),users.Credentials.passwords_list)
        
if __name__ == '__main__':
    unittest.main()        
  