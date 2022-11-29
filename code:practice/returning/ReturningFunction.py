# returningFunction1.py
# @ author:amy
# date:09.11.22

score =0

def quiz(question, answer, score):
    print(question)
    user_answer = input("Please put you answer here.")
    if user_answer == answer:
        score +=1
    else:
        print("Sorry, It is worng.")
    return score

score = quiz("What is the capital of New Zealand?","Wellington",score)
score = quiz("What do you call the scope of a variable that can be accessed anywhere in the code?","global",score)
score = quiz("What is that make function send python object back to the caller code?","Return",score)

print("\nYour score:{0}".format(score))


'''
#assertion 1
first_quiz 
Question: What is the capital of New Zealand?
Answer:Wellington

second_Quiz
Question:What do you call the scope of a variable that can be accessed anywhere in the code?
answer: I don't know

Third_Quiz
Question:What is that make function send python object back to the caller code?
Answer: Return

Your score:2
'''

