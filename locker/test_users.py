import unittest
from users import  Users
from users import  Credentials
class TestUsers(unittest.TestCase):
    '''
    TestCase that defines test cases for the user and credential class behaviours
    '''
    def setUp(self):
        '''
        setUp method to run before each cases
        '''
        self.new_account = Users("John","Facebook","jkl5")  
    def tearDown(self):
        '''
        tearDown method that cleans up after each testCase is done
        '''
        Users.accounts_list = []
       
    
    def test_init(self):
        self.assertEqual(self.new_account.username,"John")
        self.assertEqual(self.new_account.account,"Facebook")
        self.assertEqual(self.new_account.password,"jkl5")
        
    def test_save_user(self):
         '''
         To test if the account created is stored in the users list
         '''
         
         self.new_account.save_user()   
         self.assertEqual(len(Users.accounts_list),1)
         
  
    def test_save_multiple_accounts(self):
        '''
        This is to check whether multiple users can create multiple accounts
        '''
        self.new_account.save_user()
        test_user = Users("test","account","jhkl")
        test_user.save_user()
        self.assertEqual(len(Users.accounts_list),2)
       
        
    # def test_save_multiple_passwords(self):
    #     '''
    #     This was a test to check whether multiple passwords can be created
    #     '''
    #     self.new_password.save_password()
    #     test_password = Credentials("abcdefk1")
    #     test_password.save_password()
    #     self.assertEqual(len(Credentials.passwords_list),2)
    
    def test_delete_account(self):
        '''
        test_delete account to see if we can remove an account from the list
        '''
        self.new_account.save_user()
        test_account = Users("test","gmail","abc")
        test_account.save_user()
        self.new_account.delete_account()
        self.assertEqual(len(Users.accounts_list),1)
        
    # def test_delete_password(self):
    #     '''
    #     test_delete password to see if we can remove a password from the list
    #     '''
    #     self.new_password.save_password()
    #     test_password = Credentials("klcv8yio")
    #     test_password.save_password()
    #     self.new_password.delete_password()
    #     self.assertEqual(len(Credentials.passwords_list),1)
        
        
    def test_display_accounts(self):
        '''
        Method that returns a list of all saved accounts
        ''' 
        self.assertEqual(Users.display_accounts(),Users.accounts_list)
        
        
    # def test_display_passwords(self):
    #     '''
    #     Method that returns a list of all saved accounts
    #     ''' 
    #     self.assertEqual(Credentials.display_passwords(),Credentials.passwords_list)
        
if __name__ == '__main__':
    unittest.main()        
  