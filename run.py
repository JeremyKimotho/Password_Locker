#!/usr/bin/env python3.6
from main import UserInfo
from main import PasswordInfo

def create_user(username, password):
  '''
  Function to create a new user
  '''
  new_user = UserInfo(username, password)
  return new_user

def create_password(site, site_username, site_password):
  '''
  Function to create a new password
  '''
  new_password = PasswordInfo(site, site_username, site_password)
  return new_password

def password_generator(site, site_username, characters)
  '''
  Function to generate a password for a user
  '''
  characters='a1Ab2Bc3Cd4De5Ef6Fg7Gh8Hi9Ij0Jk!Km@Mn#No$Op%Pq^Q'
  new_generated_password = PasswordInfo(site, site_username, )

  def random_char(y):
       return ''.join(random.choice(string.ascii_letters) for x in range(y))


