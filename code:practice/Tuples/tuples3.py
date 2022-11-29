#tuples3.py
#authir:amy
#date:08.11.22

#Create a tuple with different data types.
Amy = ("Female", 30, "New Zealand", 64211782449)

#Create a tuple with 5numbers.Print the 3rd number.
favorite_number = (1,7,30,77,100)
print(favorite_number[2])

#Create a tuple woth 3 strings. extracts each element into a separate variables.
best_language = ("Javascript", "React", "Python")
language_1 = best_language[0]
language_2 = best_language[1]
language_3 = best_language[2]

print(language_1, " ",language_2, " ", language_3, " " )

#Create a 6 element integer tuple. Print the 4th element and 4th from last element.

lotto_balls = (1, 45, 23, 78, 34, 24)
print("The 4th lotto ball is",lotto_balls[3])
print("\nThe 4th from last lotto ball is", lotto_balls[-4])

#Print the repeated items of a tuple.
items = (1, 45, 23, 78, 34, 24, 1, 7, 30, 77, 100)
repeated_items = []
for counter in range(0,len(items)):
    for number in range(counter+1, len(items)):
        if items[counter] == items[number]:
            repeated_items.append(items[number])

individual_repeats = set(repeated_items)
print(individual_repeats)

#tuple with duplicates
items = (1, 45, 23, 78, 34, 24)
found = 0
number = int(input("Enter the value you wish to search for\n"))

for counter in range(0,len(items)):
    if items[counter] == number:
        found +=1
if found == 0:
        print("The number was not in the tuple")
elif found == 1:
        print("The number was in the tuple once")
else:
        print("The number was in the tuple more than once")



    
