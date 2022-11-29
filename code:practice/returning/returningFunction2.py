# returningFunction2.py
# @ author:amy
# date:09.11.22

print("\n$4 for the first 2 hours, then $3 for every hour thereafter.")
def parking_cost(hours):
    cost = (hours-2)*3+4

    return cost
hours = int(input("Enter the number of parking hours:"))

print("\nYour parking hours is {0} and should pay {1}".format(hours,parking_cost(hours)))

'''
Assertion
input 8
output 22

Enter the number of parking hours:
Your parking hours is 8 and should pay 22
'''
