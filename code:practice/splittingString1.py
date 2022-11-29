# splittingStrings1.py
#
# @ author: Amy
# date:12.11.22

user_input = input("Please enter 3 integerts here")

input_split = user_input.split(",")

int_input = [int(i) for i in input_split]

average = sum(int_input)/len(int_input)

print(average)

'''
#asertions1

input:Please enter 3 integerts here3,6,7
output:5.333333333333333
