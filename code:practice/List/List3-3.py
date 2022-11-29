#List3-3.py
#author:amy
#date:08.11.22

list_1=[23,66,23,12]
temp_list = []
list_to_print=[]

for item in list_1:
    if item in temp_list:
        list_to_print.append(item)
    else:
        temp_list.append(item)

print(list_to_print)
print(temp_list)
        
