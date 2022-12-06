# Parking.py
# @ author: amy
# date: 01. 11. 22

print("Kia Ora, this is a parking meter")
park_time = 9

rate = 4
cost = 0

if park_time >3:
    cost = rate*3
    rate -=2
    park_time -=3
    cost += rate * park_time
    print("The cost of the parking is $", cost)

else:
    cost = rate*park_time
    print("The cost of the parking is $", cost)

    
    
