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
  characters.string='a1Ab2Bc3Cd4De5Ef6Fg7Gh8Hi9Ij0Jk!Km@Mn#No$Op%Pq^Q'
  new_generated_password = PasswordInfo(site, site_username, def random_char(characters):
       return ''.join(random.choice(characters.string) for x in range(characters)))

def save_users(user):
  '''
  Function to save users
  '''
  user.user_save()

def save_passwords(password):
  '''
  Function to save passwords
  '''
  password.password_save()

def del_user(user):
  '''
  Function that deletes a users credentials
  '''
  user.user_delete()

def del_password(password):
  '''
  Function that deletes a password
  '''

def copy_password()
  '''
  Function that returns the copied password
  '''
  return PasswordInfo.copy_password()

def display_passwords():
  '''
  Function that returns all saved contacts
  '''
  return PasswordInfo.Passwords()

def main():
  print('Hello Welcome to password locker. To login to your account type Y, to create an account type N')
    
    response=input()

    if response == 'Y':
      print('Please enter your username')
        username=input()
      print('Please enter your password')
        password=input()

        if username in Users and password in Users:

          print(f'Welcome {username}!')
          print('\n')

          while True:
            print('Use these short codes: cp-create a new password with generation, cpg-create a new password with password generation, dp-display passwords, ex-exit the password locker.')

            short_code=input().lower()

            if short_code == 'cp':
            print('What is the site?')
              site=input()
            print('What is your username on this site?')
              site.username=input()
            print('Enter a password')
              password_1=input()
            print('Confirm password')
              password_2=input()

              if password_1 != password_2: 
                print('Your passwords did not match')
                print('Please re-enter your password')
                  password_1=input()
                print('Please confirm your password')
                  password_2=input()

                  save_passwords(site, site. username, password_1)
              else:
                save_passwords(site, site.username, password_1)

            elif short_code == 'cpg':
              print('What is the site?')
                site=input()
              print('What is your username on this site?')
                site.username=input()
              print('How many characters would you like it to have? (Between 1-14)')
                characters=input()

                save_passwords(password_generator(site, site.username, characters))

            elif short_code == 'dp':


    




  


