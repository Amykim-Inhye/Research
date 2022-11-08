#Changinglist2.py
#author:amy
#date:08.11.22

#2
proverb_part_list = ["As a man disappears", "the", "land remains."]

print("A well known Maori proberb states'...\n")
print("As a man disappears from sight the land remains\n")
print("The stored version of this proverb states'...\n")


for item in proverb_part_list:
    print(item, end=" ")

item = input("\n\nInput the first missing section of the proverb\n")
proverb_part_list.insert(1,item)
joined_list =" ".join(proverb_part_list)
print(joined_list)

#5

word = input("\ninput a word\n")
list_to_reverse = list(word)
print(list_to_reverse)
list_to_reverse.reverse()
print("".join(list_to_reverse))

#11

import random

list_1=[1,56,123,87]
list_2=[34,75,13,89]

list_1.append(list_2)
print(list_1)

list_1.extend(list_2)
print(list_1)

#13

from random import randint

lotto_balls = list(range(1,50))
print(lotto_balls)

selected_balls = []
counter =0
balls_left = 49

while counter <=6:
    ball_index= randint(1, balls_left)-1
    ball = lotto_balls[ball_index]
    if(ball)not in selected_balls:
        selected_balls.append(ball)
        lotto_balls.pop(ball_index)
    balls_left -=1
    counter +=1
print("selected ball...\n", selected_balls)
print("\nRemaining balls are...\n",lotto_balls)

