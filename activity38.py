# activity38.py
# @ author: amy
# date: 04.11.22

chosen_option = False
choice = str
side_x = int
side_x_vaild = False
side_y = int
side_y_vaild = False

print("Welcome\n\n")


while chosen_option == False:
    choice =str(input("Enter either Surface or Volume to choose."
                   "whether to calculate surface are or volume,\n\n"))
    if choice.lower() == "surface":
        chosen_option = "surface"
        chosen_option = True
    elif choice.lower() == "volume":
        chosen_option = "volume"
        chosen_option = True
    else:
        print("Incorrect choice, please try again...\n\n")

while side_x_vaild == False:
    side_x = int(input("Enter side x as an integer\n\n"))
    if side_x >=10 and side_x > 0:
        print("\nInvaild side iength\n\n")
    else:
        side_x_vaild = True

while side_y_vaild == False:
    side_y = int(input("Enter side y as an integer.\n\n"))
    if side_y >=8 and side_y > 0:
        print("\nInvaild side length\n\n")
    else:
        side_y_vaild = True

if choice == "surface":
    surface = (10 * 8 - side_x * side_y) * 2
    + ( 3 * 10 * 2) +(3 * 8 * 2) + (side_y * 3 * 2)
    print("\nThe surface area of the shape is: ", surface)

if choice == "volume":
    volume = (10 * 3 * (8 - side_y))
    + (side_y * 3 * (10 - side_x))
    print("\nThe volume of the shape is: ",volume)
  
