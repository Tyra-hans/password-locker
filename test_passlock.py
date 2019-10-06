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

if __name__ == '__main__':
    unittest.main()