# Function2.py
# @ author: amy
# date: 09.11.22

def show_hello(param):
    print("Hello there, the number of times this "
          "function is called is {0}!!!\n\n".format(param))

counter = 0
print("Testing my second user defined funtion...\n\n")
        
counter += 1

show_hello(counter)
counter +=1

show_hello(counter)
counter +=1
show_hello(counter)
