# Function3.py
# @ author: amy
# date: 09.11.22

first_number = 6
second_number = 4

def show_difference(number_1, number_2):
    print("The first number is {0}.\n"
          "The second number is {1}.\n"
          "The difference betwwen them is {2}!!!\n"
          .format(number_1, number_2, number_1-number_2))
print("Welcome to my difference calculator...\n\n")

show_difference(first_number, second_number)

print("Test case assertion : of forst number is 13 and second number is 2"
      "then the difference should ne 11!")

show_difference(13,2)
