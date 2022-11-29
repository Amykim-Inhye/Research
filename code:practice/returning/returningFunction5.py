# returningFunction5.py
# author:amy
# date: 09.11.22

print("\n Displaying values less than the average in a list\n")
list = [13, 52, 11, 58, 9, 23, 10]

def get_average(list):
    summation = 0
    for num in list:
        summation += num
    return summation / len(list)

print(get_average(list))

def get_lower_nums(average, list):
    lower_nums = []
    for num in list:
        if num < average:
            lower_nums.append(num)
    return lower_nums

average = get_average(list)
lower_nums =get_lower_nums(average, list)
print("Average: {0} \nValues less than the average:{1}."
      .format(average,lower_nums))

'''
Displaying values less than the average in a list

25.142857142857142
Average: 25.142857142857142 
Values less than the average:[13, 11, 9, 23, 10].
'''
