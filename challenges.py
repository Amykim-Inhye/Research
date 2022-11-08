# challenges.py
# @ author:amy
# 02. 11. 22

#challenge4

import math

choice = (input("You can choose the option to find out the surface area or the volume of the shape."
                "Plese choose 'surface' or 'volume.\n\n"))

if choice.lower() == 'surface':
   side_a = int(input("Enter the length of cuboid\n\n"))
   side_b = int(input("Enter the width of cuboid\n\n"))
   side_c = int(input("Enter the height of cuboid\n\n"))

   print("The surface area of the cuboid is",
         side_a*side_b*2
         +side_b*side_c*2
         +side_a*side_c*2)

if choice. lower() == "volume":
   side_a = int(input("Enter the length of cuboid\n\n"))
   side_b = int(input("Enter the width of cuboid\n\n"))
   side_c = int(input("Enter the height of cuboid\n\n"))

   print("The volume area of the cuboid is", side_a*side_b*side_c,"\n\n")

#challenge5
   
choice1 = (input("You can choose the option to find out the surface area or the volume of the shape."
                "Plese choose 'surface' or 'volume.\n\n"))

if choice1.lower() == 'surface':
    length = int(input("Enter the length of cylinder\n\n"))
    radius = int(input("Enter the radius of circle\n\n"))

    print("The surface area of the cylinder is",
          2 * math.pi * radius * length
          +2 * math.pi * radius **2,"\n\n")

if choice1.lower() == 'volume':
    length = int(input("Enter the length of cylinder\n\n"))
    radius = int(input("Enter the radius of circle\n\n"))

    print("The volume area of the cuboid is",
         math.pi * radius ** 2 * length, "\n\n")


#challenge6

choice2 = (input("You can choose the option to find out the surface area or the volume of the shape."
                "Plese choose 'surface' or 'volume.\n\n"))

if choice2.lower() == 'surface':
    base = int(input("Enter the base of the pyramid\n\n"))
    height = int(input("Enter the height of the pyramid\n\n"))

    print("The surface area of the pyramid is",
          base/2 * height * 4 + base ** 2,"\n\n")

if choice2.lower() == 'volume':
    base = int(input("Enter the base of the pyramid\n\n"))
    height = int(input("Enter the height of the pyramid\n\n"))

    print ("The volume area of the pyramid",
           base ** 2 * height/3,"\n\n")
    
