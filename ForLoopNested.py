# ForLoopNested.py
# @ author: amy
# date: 07.11.22



user_input = int(input("Please enter a number for the size"
                       "\nof the shape you wish to create."))

for i in range(user_input):
    for j in range(i):
        print("*", end=" ")
    print('')

for i in range(user_input, 0, -1):
    for j in range(i):
        print('*', end=' ')
    print('')
nl = []

for x in range (150, 200):
    if (x%7 == 0) and (x%5 == 0):
        nl.append(str(x))
print('.'.join(nl))


for fizzbuzz in range(51):
    if fizzbuzz % 3 ==0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)
