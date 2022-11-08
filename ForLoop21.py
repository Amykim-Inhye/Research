#ForLoop21.py
#author:amy
#date:07.11.22

alphabet = "";

for row in range(0,7):
    for column in range(0,7):
        if (column==1 or (row==6 and column !=0 and column<6)):
           alphabet=alphabet+"*"
        else:
            alphabet = alphabet + ""
    alphabet = alphabet+"\n"
print(alphabet)
