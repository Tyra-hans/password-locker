import unittest
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

if __name__ == '__main__':
    unittest.main()