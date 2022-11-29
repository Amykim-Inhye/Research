#Challenge2.py
# @ author: amy
# 2. 11. 22

side_a = int(input("Enter the length of the a side\n\n"))
side_b = int(input("Enter the length of the b side\n\n"))
side_c = int(input("Enter the length of the c side\n\n"))

if side_a == side_b == side_c:
    print("The triangle is equilateral\n")

if side_a == side_b and side_a != side_c\
    or side_a == side_c and side_a != side_b\
    or side_b == side_c and side_a != side_c:
    print("The triangle is isoceles\n")

if side_a != side_b != side_c:
    print("The triangle is scalar")
