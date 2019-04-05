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
    
    def test_init(self):
        self.assertEqual(self.new_account.username,"John")
        self.assertEqual(self.new_account.account,"Facebook")
        self.assertEqual(self.new_password.password,"jklmn25")
    
    def tearDown(self):
        '''
        tearDown method that cleans up after each testCase is done
        '''
        users.Users.accounts_list = []
        
        
    def test_save_user(self):
         '''
         To test if the account created is stored in the users list
         '''
         
         self.new_account.save_user()   
         self.new_password.save_password()
         self.assertEqual(len(users.Users.accounts_list),2)
    
    def test_save_multiple_accounts(self):
        '''
        This is to check whether multiple users can create multiple accounts
        '''
        self.new_account.save_user()
        self.new_password.save_password()
        
        test_user = users.Users("test","account")
        test_password = users.Credentials("abcdefk1")
        test_user.save_user()
        test_password.save_password()
        self.assertEqual(len(users.Users.accounts_list),4)
    
    def test_delete_account(self):
        '''
        test to delete an account from the account list
        '''    
        self.new_account.save_user()
        self.new_password.save_password()
        
        test_user = users.Users("test","account")
        test_password = users.Credentials("abcdefk1")
        test_user.delete_user()
        test_password.delete_password()
        self.assertEqual(len(users.Users.accounts_list),2)
if __name__ == '__main__':
    unittest.main()        
  