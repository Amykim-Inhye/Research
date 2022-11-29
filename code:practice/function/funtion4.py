# Function4.py
# @ author:amy
# date:09.11.22


score = 4

def show_new_score():
    score = 4
    score +=1
    print("You got another point...\n"
          "Your score is now {0}.\n".format(score))

x= input("Your score is {0} point...\n\n"
         "Hit any key to get another point.".format(score))
show_new_score()
