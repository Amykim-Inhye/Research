# returningFunction4.py
# author:amy
# date: 09.11.22



print('\nFinding if first number is between the second and third numbers\n')
numbers = []
def get_number_list(numbers):
   ctr = len(numbers)
   while ctr < 3:
      num = float(input('Please enter a number: '))
      if num.is_integer():
          num = int(num)
      numbers.append(num)
      ctr += 1
   return numbers
def get_within_range_truth_value(numbers):
   if numbers[2] > numbers[1]:
       if (numbers[0] >= numbers[1] and
          numbers[0] <= numbers[2]):
            return True
       else:
            return False
   else:         
       if (numbers[0] >= numbers[2] and
          numbers[0] <= numbers[1]):
            return True
       else:
            return False
numbers = get_number_list([])
print('\nIt is {0} that {1} is within the range of {2} and {3}.'
      .format(str(get_within_range_truth_value(numbers)).lower(), 
numbers[0], numbers[1],numbers[2]))

'''
#assertion
input 3,4,2
output
Finding if first number is between the second and third numbers

Please enter a number: 3
Please enter a number: 4
Please enter a number: 2

It is true that 3 is within the range of 4 and 2.

'''
