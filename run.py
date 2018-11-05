#!/usr/bin/env python3.7
from main import UserInfo
from main import PasswordInfo
import getpass

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
  characters_string='a1Ab2Bc3Cd4De5Ef6Fg7Gh8Hi9Ij0Jk!Km@Mn#No$Op%Pq^Q'
  def random_char(characters):
     generated_password = ''.join(random.choice(characters_string) for x in range(characters))
  new_generated_password = PasswordInfo(site, site_username, generated_password)
  return new_generated_password

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

def search_user(username):
  '''
  Function to search if a user exists
  '''
  return UserInfo.find_user(username)

def main():
  print(
   '''
             _____                   _____    _______                  _____                    _____                    _____                    _____          
         /\    \                 /\    \  /::\    \                /\    \                  /\    \                  /\    \                  /\    \         
        /::\    \               /::\____\/::::\    \              /::\    \                /::\____\                /::\    \                /::\    \        
       /::::\    \             /:::/    /::::::\    \            /::::\    \              /:::/    /               /::::\    \              /::::\    \       
      /::::::\    \           /:::/    /::::::::\    \          /::::::\    \            /:::/    /               /::::::\    \            /::::::\    \      
     /:::/\:::\    \         /:::/    /:::/~~\:::\    \        /:::/\:::\    \          /:::/    /               /:::/\:::\    \          /:::/\:::\    \     
    /:::/__\:::\    \       /:::/    /:::/    \:::\    \      /:::/  \:::\    \        /:::/____/               /:::/__\:::\    \        /:::/__\:::\    \    
   /::::\   \:::\    \     /:::/    /:::/    / \:::\    \    /:::/    \:::\    \      /::::\    \              /::::\   \:::\    \      /::::\   \:::\    \   
  /::::::\   \:::\    \   /:::/    /:::/____/   \:::\____\  /:::/    / \:::\    \    /::::::\____\________    /::::::\   \:::\    \    /::::::\   \:::\    \  
 /:::/\:::\   \:::\____\ /:::/    /:::|    |     |:::|    |/:::/    /   \:::\    \  /:::/\:::::::::::\    \  /:::/\:::\   \:::\    \  /:::/\:::\   \:::\____\ 
/:::/  \:::\   \:::|    /:::/____/|:::|____|     |:::|    /:::/____/     \:::\____\/:::/  |:::::::::::\____\/:::/__\:::\   \:::\____\/:::/  \:::\   \:::|    |
\::/    \:::\  /:::|____\:::\    \ \:::\    \   /:::/    /\:::\    \      \::/    /\::/   |::|~~~|~~~~~     \:::\   \:::\   \::/    /\::/   |::::\  /:::|____|
 \/_____/\:::\/:::/    / \:::\    \ \:::\    \ /:::/    /  \:::\    \      \/____/  \/____|::|   |           \:::\   \:::\   \/____/  \/____|:::::\/:::/    / 
          \::::::/    /   \:::\    \ \:::\    /:::/    /    \:::\    \                    |::|   |            \:::\   \:::\    \            |:::::::::/    /  
           \::::/    /     \:::\    \ \:::\__/:::/    /      \:::\    \                   |::|   |             \:::\   \:::\____\           |::|\::::/    /   
            \::/____/       \:::\    \ \::::::::/    /        \:::\    \                  |::|   |              \:::\   \::/    /           |::| \::/____/    
             ~~              \:::\    \ \::::::/    /          \:::\    \                 |::|   |               \:::\   \/____/            |::|  ~|          
                              \:::\    \ \::::/    /            \:::\    \                |::|   |                \:::\    \                |::|   |          
                               \:::\____\ \::/____/              \:::\____\               \::|   |                 \:::\____\               \::|   |          
                                \::/    /  ~~                     \::/    /                \:|   |                  \::/    /                \:|   |          
                                 \/____/                           \/____/                  \|___|                   \/____/                  \|___|          
                                                                                                                                                          '''
  )
  while True:
    print('Hello Welcome to password locker. To login to your account type Y, to create an account type N, to exit type E')
      
    response=input().upper()

    if response == 'Y':
      print('Please enter your username')
      username=input()
      password = getpass.getpass(prompt='Please enter your password') 
      # print('Please enter your password')
      # password=input()

      search_result=search_user(username)

      if search_result == True:

        print(f'Welcome {username}!')
        print('\n')

        while True:
          print('Use these short codes: cp-create a new password without generation, cpg-create a new password with password generation, dp-display passwords, ex-exit the password locker.')

          short_code=input().lower()

          if short_code == 'cp':
            print('What is the site?')
            site=input()
            print('What is your username on this site?')
            username=input()
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

              save_passwords(create_password(site, username, password_1))
              print('\n')
              print('Password Successfully Saved!')
              print('\n')
            else:
              save_passwords(create_password(site, username, password_1))
              print('\n')
              print('Password Successfully Saved!')
              print('\n')

          elif short_code == 'cpg':
            print('What is the site?')
            site=input()
            print('What is your username on this site?')
            username=input()
            print('I have autogenerated a password for you. To view this passwords visit the display section.')
            print('\n')
            characters='Ab2Bc3Cd4De5Ef6Fg7Gh8'

            save_passwords(create_password(site, username, characters))

          elif short_code == 'dp':
            if display_passwords():
              print('Here are your passwords:')
              print('\n')

              for Passwords in display_passwords():
                print(f'For {Passwords.site} your username is {Passwords.site_username} and password {Passwords.site_password}')
                print('\n')
            else:
              print('\n')
              print('You don\'t have any passwords to show')
              print('\n')

          elif short_code == 'ex':
            print('I\'ll miss you.....')
            print('\n')
            break

          else:
            print('I didn\'t quite get that, please refer to the shortcodes.')
            print('\n')
            break

      else:
        print('That is an incorrect username or password')
        print('\n')
        continue
      
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
        print('\n')
        continue
      else:
        save_users(create_user(username, password_1))
        print('You\'re now able to login')
        print('\n')
        continue

    elif response == 'E':
      print('Sad to see you go!')
      print('\n')
      print(
        '''
  _____                        _                _      _____                   
/  __ \                      | |              | |    /  ___|                  
| /  \/ ___  _ __ ___   ___  | |__   __ _  ___| | __ \ `--.  ___   ___  _ __  
| |    / _ \| '_ ` _ \ / _ \ | '_ \ / _` |/ __| |/ /  `--. \/ _ \ / _ \| '_ \ 
| \__/\ (_) | | | | | |  __/ | |_) | (_| | (__|   <  /\__/ / (_) | (_) | | | |
 \____/\___/|_| |_| |_|\___| |_.__/ \__,_|\___|_|\_\ \____/ \___/ \___/|_| |_|
                                                                              
                                                                              
        '''
      )

      break
    
    else:
      print('I don\'t understand that, I\'ll assume you\'re saying goodbye. Sad to see you go!' )
      print('\n')
      print(
        '''
         _____                        _                _      _____                   
/  __ \                      | |              | |    /  ___|                  
| /  \/ ___  _ __ ___   ___  | |__   __ _  ___| | __ \ `--.  ___   ___  _ __  
| |    / _ \| '_ ` _ \ / _ \ | '_ \ / _` |/ __| |/ /  `--. \/ _ \ / _ \| '_ \ 
| \__/\ (_) | | | | | |  __/ | |_) | (_| | (__|   <  /\__/ / (_) | (_) | | | |
 \____/\___/|_| |_| |_|\___| |_.__/ \__,_|\___|_|\_\ \____/ \___/ \___/|_| |_|
                                                                              
                                                                              
        '''
      )

if __name__=='__main__':
    main()



      




  


