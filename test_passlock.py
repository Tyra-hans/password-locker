import unittest
from passlock import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
    unittest.TestCase: TestCase class that helps in creating test cases
        
    '''

    def setUp(self):
        '''
        set up method to run before eavh test cases.
        '''
        self.new_user = User('Tyra','12344')

if __name__ == '__main__':
    unittest.main()