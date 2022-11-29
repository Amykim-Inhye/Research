# ExceptionExample3.py
#
# @ author: Amy
# date: 13.11.22

entry_is_valid = False
number_of_goes = 0

while not entry_is_valid:
    try:
        number_entered = int(input("Enter a vaild positive integer\n"))
        if number_entered <=0:
            raise ValueError("Entered value is not a positive integer.")
    except ValueError as e:
        print("The entry is not valid:\n{0}\n"
              "Please try again..."
              .format(e))
    else:
        entry_is_valid = True
        print("Thank you. The acceptable number entered "
              "was {0}.".format(number_entered))
    finally:
        number_of_goes+=1
        print("The number of goes used is ...{0}.".format(number_of_goes))
'''
assertion1
input:
Enter a vaild positive integer
3
output:
Thank you. The acceptable number entered was 3.
The number of goes used is ...1.

assertion2

input:
Enter a vaild positive integer
0
output:
The entry is not valid:
Entered value is not a positive integer.
Please try again...
The number of goes used is ...1.
Enter a vaild positive integer
'''
