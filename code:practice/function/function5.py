# Function5.py
# @ author:amy
# date:09.11.22

score = 4

def get_new_score(param_score):
    param_score +=1
    print("You got another point...\n"
          "Your score is now {0}.\n".format(param_score))
    return param_score

x = input("Your score is {0} points...\n\n"
          "Hit any key to get another point.".format(score))

score = get_new_score(score)

#'''
print("Test case accertion: the current score is 5\n"
      "and it should become 6!!")
score = get_new_score(score)

#'''
