import unittest
from main import UserInfo
import pyperclip

class TestData(unittest.TestCase):
  '''
  Test class that defines test cases for the contact class behaviours.

  Args:
  unittest.TestCase: TestCase class that helps in creating test cases
  '''

  def setUp(self):
    '''
    This is a set up method to run before each test case.
    '''
    self.new_user = UserInfo('Jeremy', '12345')
  
  def tearDown(self):
    '''
    That erases the data after each test case has run.
    '''
    UserInfo.Users=[]

  def test_init(self):
    '''
    test case to see if the object is correctly initialised.
    '''
    self.assertEqual(self.new_user.username,'Jeremy')
    self.assertEqual(self.new_user.password,'12345')

if __name__ == '__main__':
  unittest.main()