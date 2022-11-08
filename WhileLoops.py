#WhileLoops.py
# @ author: amy kim
# date 04. 11. 22


is_running = True

while is_running:
    answer = input("What is the meaning of life? \n")
    if answer == "42":
        print("Correct! Well done!\n")
        is_running = False
        
    else: print("Sorry that is the wrong answer.."
                "\nTry again!\n")

x = input("Press any key to exit.")


number_of_tries = 3

while True:
    answer = input("What is the meaning of life?\n")
    if answer == "42":
        print("Correct!\n")
        break
    else:
        print("Sorry that is the wrong answer\n")

        number_of_tries -=1

    if number_of_tries == 0:
        print("You have run out of goes. Sorry")
        break
        
