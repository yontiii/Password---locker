from users import Credentials
import unittest

class CredentialsTest(unittest.TestCase):
    '''
    class that will inherit methods from testcase
    '''
    def setUp(self):
        '''
        method that setups a new instance of the class
        before the tests are run
        '''
        self.new_credentials = Credentials("jump","ig","memes@me.com")
        
    def tearDown(self):
        '''
        teardown that cleans up after every testcase is done
        '''
        Credentials.Credentials_list =  []

    def test_init(self):
        self.assertEqual(self.new_credentials.magicword,"jump")
        self.assertEqual(self.new_credentials.account,"ig")
        self.assertEqual(self.new_credentials.email,"memes@me.com")
        
    def test_save_credentials(self):
        '''
        function to save the credentials created
        '''
        self.new_credentials.save_credential()
        self.assertEqual(len(Credentials.Credentials_list),1)
    
    def test_save_multiple_credentials(self):
        '''
        Function to save more than one account credential
        '''
        self.new_credentials.save_credential()
        test_credential = Credentials("test","account","test@me.com")
        test_credential.save_credential()
        self.assertEqual(len(Credentials.Credentials_list),2)
        
    def test_delete_credential(self):
        self.new_credentials.save_credential()
        test_credential = Credentials("test","account","test@me.com")
        test_credential.save_credential()
        self.new_credentials.delete_credential()
        self.assertEqual(len(Credentials.Credentials_list),1)
        
    
        
        
    
if __name__ == '__main__':
    unittest.main()