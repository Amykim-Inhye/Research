# Quiz.py
# @ author : amy
# date : 01.11.22

from datetime import datetime

score = 0
start_time = datetime.today()

answer_one = (input("What is the capital of new zealand?\n\n"))

if answer_one.lower()== 'wellington':
    score = score+1
    print("\nThat is correct. Your current score is ", score)
else:
    print("\nThat is incorrect. Your current score is still", score)


answer_two = int(input("How long time differrent hour in NZ and Korea?\n\n"))

if answer_two == 4:
    score = score+1
    print("\nThat is correct. Your current score is ", score)
else:
    print("\nThat is incorrect. Your current score is still", score)

answer_three = (input("New Zealand is islands, Please answer yes or no.\n\n"))

if answer_three.lower() == "yes":
    score = score+1
    print("\nThat is correct. Your current score is ", score)
else:
    print("\nThat is incorrect. Your current score is still", score)

answer_four = (input("What is the name of the New Zealand Rubgy team?\n\n"))
if answer_four.lower() == "all blacks":
    score = score+1
    print("\nThat is correct. Your current score is ", score)
else:
    print("\nThat is incorrect. Your current score is still", score)


answer_five = int(input("What is the population of New Zealand?\n\n"))
if answer_five == 5080000:
 score = score+1
 print("\nThat is correct, Your current score is ", score)
else:
    print("\nThat is incorrect, Your current score is still", score)
    
print("\nYour final score is ", score ,"\n\n")
print("The time taken for you to complete this quiz is....", datetime.today() - start_time)
