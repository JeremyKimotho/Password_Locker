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

  def test_user_save(self):
    '''
    this test case will be testing if saving a users username and password is possible and done into the user object
    '''
    self.new_user.user_save()
    self.assertEqual(len(UserInfo.Users),1)

  def test_multiple_user_save(self):
    '''
    this test case will be used to test if multiple users can be saved if need be 
    '''
    self.new_user.user_save()
    test_user = UserInfo('Test', 'Tester')
    test_user.user_save()
    self.assertEqual(len(UserInfo.Users),2)

  def test_delete_user(self):
    '''
    this test case to make sure a user can be deleted
    '''
    self.new_user.user_save()
    test_user = UserInfo('Test', 'Tester')
    test_user.user_save()
    self.new_user.delete_contact()
    self.assertEqual(len,(UserInfo.Users),1)

if __name__ == '__main__':
  unittest.main()