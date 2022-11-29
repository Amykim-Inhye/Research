# MoreFunctionPracticeChallenge1.py
# Author:Amy
# date: 10.11.22

list_1 = [5, 10, 15, 20, 25]

def get_first_last(list_1):
    list_2=[list_1[0],list_1[-1]]
    return list_2

combined_list = get_first_last(list_1)
print(combined_list)

'''
#assertions
input:list_1 = [5, 10, 15, 20, 25]
output:[5, 25]
'''
