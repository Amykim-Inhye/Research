# ImprovedCalculator.py
#
# @ author: Amy
# date:12.11.22

def do_calculation(user_input): 
    calculated_answer = int

    split_input=user_input.split()

    input_params = split_input[1].split(",")
    
    if split_input[0] == "add":
        calculated_answer = int(input_params[0]) + int(input_params[1])
    elif split_input[0] == "subtract":
        calculated_answer = int(input_params[0])-int(input_params[1])
    else:
        return "Unknown command entered!"
    return calculated_answer

user_input = input("Please enter an operation and 2 parameters\n")
print("The answer is :{0}".format(do_calculation(user_input)))
