# Login1.py
# @ author: amy
# date: 09.11.22


loginDetails = {'user1':'apple123', 'user2':'ball456', 'user3':'coin789'}
print('\nWelcome! You have three attempts to enter your login details.')
attempt = 0
while attempt < 3:
  print('\nPlease enter your Username and Password:')
  user_name = input('\nUsername: ')
  password = input('Password: ')
  success = False
  for key,value in loginDetails.items():
    if (key == user_name 
       and value == password):
         success = True
         break
  attempt += 1
  if not success:
    if attempt < 3:  
      print('\nSorry, login unsuccessful, please try again\n')
    else:  
      print('\nSorry, that was your third attempt!')
  else:
      break
      
if success:
    print('\nCongratulations, you have sucessfully logged in!')
