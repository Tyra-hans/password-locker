import unittest
import pyperclip
from passlock import Credential

class TestCredential(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.
    
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases

    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credential('Facebook','Tyra-hans', '12344')#create credential object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.title,'Facebook')
        self.assertEqual(self.new_credential.username,'Tyra-hans')
        self.assertEqual(self.new_credential.password,'12344')

    def tearDown(self):
        '''
        tearDown method that does clean up after each testcase has run.
        '''
        Credential.credential_list=[]
        

    def test_save_credential(self):
        '''
        test_save_credential test case to test if the credential save object is saved into credential list
        '''
        self.new_credential.save_credential() #saving the new credential
        self.assertEqual(len(Credential.credential_list),1)

    def test_save_multiple_credentials(self):
        '''
        test_save_multiple_credentials to check if the user can save multiple credential
        objects to credential list
        '''
        self.new_credential.save_credential()
        test_credential = Credential('twitter','hanstyra','12345')
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),2)

    def test_delete_credential(self):
        '''
        test_delete_credential to test if we can remove a credential from our credential list
        '''
        self.new_credential.save_credential()
        test_credential = Credential('test','user','1234')
        test_credential.save_credential()

        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.credential_list),1)

    def test_find_credential_by_title(self):
        '''
        test to check if we can find credential by it's titleand display
        '''

        self.new_credential.save_credential()
        test_credential = Credential('twitter','tyrahans','0987')
        test_credential.save_credential()

        found_credential = Credential.find_by_title('twitter')
        self.assertEqual(found_credential.username,test_credential.username)

    def test_credential_exists(self):
        '''
        test to check if we can return a Boolean if we cannot find the contact.
        '''

        self.new_credential.save_credential()
        test_credential = Credential('test', 'username','2345')
        test_credential.save_credential()

        credential_exists = Credential.credential_exist('test')

        self.assertTrue(credential_exists)

    def test_display_credentials(self):
            '''
            method that returns a list of all contacts saved
            '''

            self.assertEqual(Credential.display_credentials(),Credential.credential_list)

    def test_copy_username(self):
        '''
        Test to confirm that we are copying the credential
        '''

        self.new_credential.save_credential()
        Credential.copy_username('title')
        
        self.assertEqual(self.new_credential.username,pyperclip.paste())



if __name__ == '__main__':
    unittest.main()