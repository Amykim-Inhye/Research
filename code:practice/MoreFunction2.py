# MoreFunctionPracticeChallenge2.py
# Author:Amy
# date: 10.11.22

list_1=[4, 9, 7]

def histogram(list_1):
    for count in range(0,len(list_1)):
        for item_count in range (0, list_1[count]):
            print("*",end="")
        print("")

histogram(list_1)
