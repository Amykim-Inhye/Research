# Exception1.py
#
# @ author:Amy
# date: September 2016

def divide_numbers(number_1, number_2):
    try:
        return number_1/number_2
    except ZeroDivisionError:
        return "Error, cannot divide by zero!"
    except TypeError as e:
        message = "Error, an operand is the wrong type...\n"\
                  "Or as python would say...\n{0}".format(e)
        return message

print(divide_numbers(3,0))
