# Fibonacci Using While
# @ author: amy
# date: 07.11.22

print("\nThe Fibonacci Sequence:\n")
p = "0"
while int(p) < 3:
    p= input("Please enter a number corresponding to the position in the sequence(should be at lease 3:)")

    q = 0
while q <=0:
    q = int(input("Please enter number of terms to generagte(should be a positive integer):"))
    print("\n", q, 'number in the sequence starting from term', p , ':')
p, q = int(p), int(q)

p_counter, q_counter = 2, 0

n1, n2 = 0 ,1


while q_counter < p:
    nth = n1 + n2
    n1, n2 = n2, nth
    p_counter +=1
    if p_counter >= p:
        q_counter +=1
        if q_counter < q:
            print(nth, end = ", ")
        else:
            print(nth)
