# Challenge1.py
# @ author: amy
# date: 02 11 22

row_letter = 0
choice_row = (input("Enter the row letter of the square\n\n"))

if choice_row.lower() == ("a" or "c" or "e" or "g"):
    row_letter = 1

choice_col = int(input("Enter the column number of the square\n\n"))
coordinates = choice_col + row_letter

if coordinates%2 == 0:
    print("The square is black""\n\n")
else:
    print("The square is white""\n\n")
