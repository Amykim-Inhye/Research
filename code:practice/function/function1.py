#function1.py
#author:amy
#date:09.11.22


def show_hello():
    print("Hello there, this is very first function!!\n\n")


show_hello()
show_hello()

#task2.

print("\nWelcome to function world!")

def add_number(a,b):
    return a+b

print(add_number(3,5))

def store(y="text" ,x=1):
    print(y,"is a text and ",x," is a number of times")
store(y="hello", x = 8)


import random

def r():
 num = random.random()
 return num

print(r())
 
