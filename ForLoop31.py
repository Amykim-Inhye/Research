#ForLoop31.py
#author: amy
#date:07.11.22

human_age = int(input("Input a dog's age in human years: "))

if human_age < 0:
    print("Age must be positive number.")
    exit()
elif human_age <= 2:
    dog_age = human_age * 10.5
else:
    dog_age = 21 +(human_age - 2)*4

print("The dog's age in dog's years is", dog_age)
