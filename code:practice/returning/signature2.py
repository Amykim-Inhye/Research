# Signatures2.py
#
# @ author:amy
# date:09.11.22
 
def show_young_age(my_age):
    print("My age 10 years ago was {0}.\n".format(my_age-10))
show_young_age(22)

def show_future_age(my_age):
    print("My age 10 years more will be {0}.".format(my_age+10))
show_future_age(30)

def amy_boyfirend(age, his_name):
    print("\nHe is 2 years older tnan Amy")
    print("Amy's boyfirend is {0} and his name is {1}.".format(age+2,his_name))
amy_boyfirend(30,"JK")


import math

def overLoadExample(length, height):
    return length*height

print(overLoadExample(10,30))

def overLoadExample(length, height, depth):
    return length * height * depth

print(overLoadExample(3,4,10))
print(overLoadExample(5,30))
