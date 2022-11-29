#List3-8.py
#author:amy
#date:08.11.22

import random

list =[1,19,4,8]

item_1 = (random.choice(list))
item_2 = (random.choice(list))

while item_1 == item_2:
    item_2 = (random.choice(list))

print(item_1,"",item_2)
