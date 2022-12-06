#SearchingString1.py
#author:amy
#date:11.11.22

store = "The first rule of fight club is: do not talk about fight club."
print("he number of times that a space appears is {0}.".format(store.count(" ")))


'''
#assertions1
store = "The first rule of fight club is: do not talk about fight 
club."
Output: The number of times that a space appears is 12
'''

user_input = input("Please enter some text\n")

print("Does this string start with the given text?\n{0}".format(store.startswith(user_input)))

'''

#Assertions3
Input: The
Output: Does this string start with the given text?
True
'''

find_fight_index =store.find("fight")
print("The index position of the fight is{0}\n".format(find_fight_index))
'''
#Assertions5
Input: store = "The first rule of fight club is: do not talk about fight club."
Output:The index position of the fight is18
'''
