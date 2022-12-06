# MoreFunctionPracticeChallenge5.py
# Author: Amy
# date: 11.11.22

list_word = ["python", "Javascript", "React", "html"]
list_lengths = []

def word_length(list_word):
    for count in range (0, len(list_word)):
        num = len(list_word[count])
        list_lengths.append(num)
        
word_length(list_word)
print(list_lengths)

'''
#assertions
input:list_word= ["python", "Javascript", "React", "html"]
output:[6, 10, 5, 4]
