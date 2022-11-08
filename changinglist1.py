#Changinglist1.py
#author:amy
#date:08.11.22

list_1 = [34, 123, 5, 77, 59, 2, 4]

print(list_1[2:5])

#2
length = len(list_1)
half = (int(length/2))
print(half)
print(list_1[0:half])
print(list_1[0:3])

#3
list_extra=(42,1,2,19,108)
list_1.extend(list_extra)

print(list_1)

length = len(list_1)
if length%4 == 0:
    quarter = (int(length/4))
    three_quarters = quarter*3
    print(list_1[three_quarters:length])
    print(list_1[9:12])
