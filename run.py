#!/usr/bin/env python3.7
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

def password_generator(site, site_username, characters):
  '''
  Function to generate a password for a user
  '''
  characters.string='a1Ab2Bc3Cd4De5Ef6Fg7Gh8Hi9Ij0Jk!Km@Mn#No$Op%Pq^Q'
  def random_char(characters):
    return generated_password == ''.join(random.choice(characters.string) for x in range(characters))
  new_generated_password = PasswordInfo(site, site_username, generated_password)

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

def copy_password():
  '''
  Function that returns the copied password
  '''
  return PasswordInfo.copy_password()

def display_passwords():
  '''
  Function that returns all saved contacts
  '''
  return PasswordInfo.display_passwords()

def main():
  while True:
    print('Hello Welcome to password locker. To login to your account type Y, to create an account type N, to exit type E')
      
    response=input().upper()

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
            if display_passwords():
              print('Here are your passwords')
              print('\n')

              for PasswordsInfo in display_passwords():
                print(f'For {passwords.site} your username is {passwords.site_username} and password {passwords.site_password}')
                print('\n')
            else:
              print('\n')
              print('You don\'t have any passwords to show')
              print('\n')

          elif short_code == 'ex':
            print('I\'ll miss you.....')
            break

          else:
            print('I didn\'t quite get that, please refer to the shortcodes.')
            break

      else:
        print('That is an incorrect username or password')
        break
      
    elif response == 'N':
      print('Please enter a username')
      username=input()
      print('Please enter a password')
      password_1=input()
      print('Please confirm your password')
      password_2=input()

      if password_1 != password_2:
        print('Your passwords didn\'t match')
        print('Please enter a password')
        print('Please confirm password')
        save_users(create_user(username, password_1))
        print('You\'re now able to login')
        break
      else:
        save_users(create_user(username, password_1))
        print('You\'re now able to login')
        break

    elif response == 'E':
      print('Sad to see you go!')
      break
    
    else:
      print('I don\'t understand that, I\'ll assume you\'re saying goodbye. Sad to see you go!' )

if __name__=='__main__':
    main()



      




  


