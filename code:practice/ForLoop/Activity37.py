# Activity37.py
# @ author: amy
# date 03. 11. 22



password = (input("Please enter a password.\n\n"))
limited =0
correct = False

while limited<2 and correct == False:
    if password == "amy123":
     correct = True
    elif password == "Exit":
        print("\nProgramme terminated.\n\n")
        correct = True
    else:
        print("\nIncorrect password.\n\n")
        password = (input("Please enter a pssword\n\n"))
        limited +=1

        
guess = int(input("Guess a number\n\n"))
last_guess = int
secret_number = 91
counter = 0
found = False

while found != True :
    if guess > secret_number:
        print("\nToo high try again.\n\n")
        if last_guess !=guess:
            counter +=1
         
    elif guess < secret_number:
        print("\nToo low try again.\n\n")
        if last_guess !=guess:
            counter +=1
        
    else:
        counter +=1
        print("\nThat is correcct!.\n\n")
        found = True

print("\nYou had", counter, "guesses\n\n")
    
        
  
        
