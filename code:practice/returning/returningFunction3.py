# returningFunction3.py
# @ author:amy
# date:09.11.22

from time import sleep

print("Welcome to Count Down Timer.")

def timer():
    seconds = int(input("Please enter the number of seconds to count down."))

    return(seconds)
def countdown_exit(seconds):
    start = seconds
    print("\nStart\n")
    for counter in range(seconds):
        now = start-counter
        print(now)
        sleep(1)
    print("Time up!")
    return 0

print("\nProceess finished with exit code {0}".format(countdown_exit(timer())))


'''
#Assertions
input 5
output
Welcome to Count Down Timer.
Please enter the number of seconds to count down.5

Start

5
4
3
2
1
Time up!

Proceess finished with exit code 0
'''
