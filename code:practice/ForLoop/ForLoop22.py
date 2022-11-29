#ForLoop22.py
#author:amy
#date:08.11.22

alphabet=""
for row in range(0,7):
    for column in range(0,7):
        if(column == 1 or column == 5 or (row == 2 and (column == 2 or column == 4)) or (row == 3 and column ==3)):
             alphabet = alphabet + "*"
        else:
             alphabet = alphabet+" "
    alphabet = alphabet+"\n"
print(alphabet)
