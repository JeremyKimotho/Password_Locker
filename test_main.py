import unittest
from main import UserInfo
import pyperclip
from main import PasswordInfo

class TestUser(unittest.TestCase):
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
    self.new_user.user_delete()
    self.assertEqual(len(UserInfo.Users),1)

class TestPassword(unittest.TestCase):
  '''
  test class that defines the test cases for the password class behaviours.

  Args:
  unittest.TestCase: TestCase class that helps in creating test cases
  '''

  def setUp(self):
    '''
    Set up method to run before we start every test
    '''
    self.new_password = PasswordInfo('Instagram', 'jkim', '12345')

  def tearDown(self):
    '''
    Tear down method that cleans up after each test case
    '''
    PasswordInfo.Passwords=[]

  def test_init(self):
    '''
    this is testing to see if the object is correctly being initiated
    '''
    self.assertEqual(self.new_password.site,'Instagram')
    self.assertEqual(self.new_password.site_username,'jkim')
    self.assertEqual(self.new_password.site_password,'12345')

  def test_save_password(self):
    '''
    this test case is being used to test if the passwords are being saved correctly, along with the associating site and username info
    '''
    self.new_password.password_save()
    self.assertEqual(len(PasswordInfo.Passwords),1)

  def test_multiple_password_save(self):
    '''
    this test case is to ensure it's possible to save multiple passwords 
    '''
    self.new_password.password_save()
    test_password = PasswordInfo('Te', 'Tes', 'Test')
    test_password.password_save()
    self.assertEqual(len(PasswordInfo.Passwords),2)

  def test_password_delete(self):
    '''
    this test case is to make usre that if need be, a password can be deleted.
    '''
    self.new_password.password_save()
    test_password=PasswordInfo('Te', 'Tes', 'Test')
    test_password.password_save()
    self.new_password.password_delete()
    self.assertEqual(len(PasswordInfo.Passwords),1)

  def test_copy_password(self):
    '''
    this is a test to confirm that the pyperclip module is correctly copying the password
    '''
    self.new_password.password_save()
    PasswordInfo.copy_password('12345')
    self.assertEqual(self.new_password.site_password, pyperclip.paste())

if __name__ == '__main__':
  unittest.main()