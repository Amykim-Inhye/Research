#Trianngles.py
# author: amy
# date: 07. 11. 22

print("Input lengths of the triangle sides: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x == y == z:
    print("Equilateral triangle")
elif x ==y or y ==z or z ==x:
    print("isosceles triangle")
else:
    print("Scalene triangle")
    

print("Input sime integers to calculate their sum and average. Input 0 to exit.")

count = 0
sum = 0.0
number = 1

while number != 0:
    number = int(input(""))
    sum = sum+number
    count += 1

if count == 0:
    print("Input some number")
else:
    print("Average and Sum of the above numbers are: ", sum / (count-1), sum)
