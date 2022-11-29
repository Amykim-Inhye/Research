#ForLoop27.py
#author:amy
#date:08.11.22

alphabet =""

for row in range(0,7):
    for column in range(0,7):
        if(column==3 or(row==0  and column>0 and column<6)):
            alphabet = alphabet+"*"
        else:
            alphabet =alphabet+" "
        
    print(alphabet)
