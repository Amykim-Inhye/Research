#Changinglist.py
#author:amy
#date:08.11.22

from datetime import datetime, timedelta
duration =10
run = input("Enter 'start' to begin\n")
period = timedelta(seconds=1)

next_time = datetime.now() + period

counter = 0
while run == "start" and counter < duration:
    if next_time <=datetime.now():
        print("..", counter)
        counter += 1

        next_time += period
