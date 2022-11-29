#Dictionary2.py
#author:amy
#date:08.11.22

#5
todo_list = {"3pm":"attend a meeting", "12pm":"go to bank", "5pm":"work out"}
for value in todo_list:
    print("\nToday, I should", todo_list[value])

del(todo_list["3pm"])
print("\nDone to-do be removed.",todo_list)

todo_list["9pm"] = "go to sleep"

todo_list["12am"] = "go to sleep"

print(todo_list)
      

#4

city_dict = {"AKL":1495, "CLC":3234.8,"DUD":1238}
print(city_dict)

sum = 0
for popn in city_dict.values():
    sum += popn
print(sum)
