import pyperclip

class UserInfo:
  '''
  Class that generates when a user would like to add their info which is used to verify their identity, before giving them password info.
  '''
  
  Users=[]

  def __init__(self, username, password):
    self.username = username
    self.password = password 

  def user_save(self):
    '''
    this method will save my users info
    '''
    UserInfo.Users.append(self)

  def user_delete(self):
    '''
    this method will delete my users info
    '''
    UserInfo.Users.remove(self)

class PasswordInfo:
  '''
  Class that generates when a user would like to add or delete or view a password they have stored
  '''
  Passwords = []

  def __init__(self, site, site_username, site_password):
    self.site = site
    self.site_username = site_username
    self.site_password = site_password

  def password_save(self):
    '''
    this method saves a password details objects into the Passwords list
    '''
    PasswordInfo.Passwords.append(self)

  def password_delete(self):
    '''
    this method makes it possible to delete any passwords we may not want anymore
    '''
    PasswordInfo.Passwords.remove(self)

  @classmethod
  def copy_password(cls, number):
    pyperclip.copy(number)


  