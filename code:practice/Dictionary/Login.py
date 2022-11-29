# Login.py
# @ author: amy
# date: 09.11.22

loginDetails = {'user1':'apple123','user2':'ball456','user3':'coin789'}

print("\nWelcome! You have three attempts to enter you login details.")

attempt = 0
while attempt <3:
    print("\nPlease enter your Username and Password:")
    user_name = input("\nUser name:")
    password = input("Password:")
    success = False
    for key, valuse in loginDetails.items():
        if(key == user_name
            and value == password):
            success = True
            break
    attempt += 1
    if not success:
        if attempt <3:
            print("\nSorry, login unsuccessful, Please try again\n")
        else:
            print("\nSorry, That was your third attempt!")
    else:
        break
               
if success:
    print("\nCongratualtions, you have sucessfully logged in!")
          
