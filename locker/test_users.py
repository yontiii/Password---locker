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
       
    
    def test_delete_account(self):
        '''
        test_delete account to see if we can remove an account from the list
        '''
        self.new_account.save_user()
        test_account = Users("test","gmail","abc")
        test_account.save_user()
        self.new_account.delete_account()
        self.assertEqual(len(Users.accounts_list),1)
        
        
    def test_display_accounts(self):
        '''
        Method that returns a list of all saved accounts
        ''' 
        self.assertEqual(Users.display_accounts(),Users.accounts_list)
        
        
    def test_find_account(self):
        '''
        test to check if we can find an account using the username
        '''
        self.new_account.save_user()
        test_account = Users("john","facebook","jklm")
        test_account.save_user()
        
        found_account = Users.find_by_account("facebook")
        self.assertEqual(found_account.username,test_account.username)
        
    def test_account_exixts(self):
        '''
        test to check if we can return a boolean if we can not find the contact
        '''
        self.new_account.save_user()
        test_account = Users("Test","account","jk25")
        test_account.save_user()
        account_exists = Users.account_exist("account")
        self.assertTrue(account_exists)
        
if __name__ == '__main__':
    unittest.main()        
  