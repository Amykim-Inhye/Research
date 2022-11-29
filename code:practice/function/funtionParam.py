# Functions With Parameters
# Challenge 1 
# author: amy
# date: 09.11.22

name = input("\n Please enter your name:")
phone_number=input("please enter your phone number:")

def display(name, phone_number):
    print("\nHello there, My name is {0} and my phone number is {1}."
          .format(name, phone_number.rstrip()))

display(name,phone_number)

'''
#Assertion1
print("\nTest case assertion 1 - input and output shown below.\n\n")
print("Pleas enter you name: Amy\n",
    "please enter you phone number: 0211782249\n\n",
    "Hello therem My name is amy and my phone number is 0211782440.")
'''


base =int(input("\nPlease enter a any number:"))
times =int(input("\nPlease enter the number of multiples to generate:"))

def display_multiples(base, times):
    counter = 1
    number = base
    while counter <= times:
        number += base
        counter += 1
        print(number)

display_multiples(base, times)

'''
#Assertion3
print("\nTest case assertion 3 - input and output shown below.\n\n")
print("Please enter a number:2",
        "\nPlease the number of multiples to generate:4",
        "4\n",
        "6\n",
        "8\n",
        "10\n",
        
'''

print("Counting Even number from this list:")

numbers = [2,25,75,83,24,33,22,80,92]

def even_number(x):
    counter = 0
    for index, item in enumerate(x):
     if (isinstance(x[index],int)and (x[index]%2) ==0):
        counter +=1
    print("\nThe counter of even number is:{0}".format(counter))
even_number(numbers)


'''
#Assertion6
print("\nTest case assertion 6 - input and output shown below.\n\n")
print("Counting even numbers from list.",
    "\n[2,25,75,83,24,33,22,80,92]\n",
    "The count of even number is:5")
'''
