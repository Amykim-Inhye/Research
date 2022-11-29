#ForLoop36.py
#author:amy
#date:07.11.22

print("Input lenghts of the triangle sides: ")
x= int(input("x: "))
y= int(input("y: "))
z= int(input("z: "))

if x==y==z:
    print("Equilateral triangle")
elif x==y or y==z or z==x:
    print("isosceles triangle")
elif x+y > z or y+z > x or z+x>y:
    print("This is Scalene triangle and the Longest triangle side is smaller than the sum of the other 2 sides")
else:
    print("Scalene triangle")

