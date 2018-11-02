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
    