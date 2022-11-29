#List3.py
#author:amy
#date:08.11.22

list_1=[23, 66, 23, 12]
list_2=[1, 19, 4, 8]
list_sum=(sum(list_1)+sum(list_2))


user_input = input("Type Sum or Average.\n\n")

if user_input.lower()=="sum":
    print(list_sum)

if user_input.lower()=="average":
    average = float(list_sum)/(len(list_1)+len(list_2))
    print(average)

list_3=["land of", "the", "the long white cloud"]
temp_list=[list_2, list_3]
print(temp_list)


list_to_print = []
print(list_to_print)

for item in temp_list:
    if len(item) > len(list_to_print):
        list_to_print = item
        
print(item)
print(list_to_print)

