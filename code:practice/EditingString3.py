#EditingString3 .py
#
# @ author: Amy
# date: 11.11.22

"Welcome <first_name>. Thank you for joining <bank_name>. Your balance is $<balance>"
bank_records = [["Amy","ANZ", 10000],["JK","ASB",39999],["Brody","KIWI Bank",10900]]

for count in range(0, len(bank_records)):
    list_1 = bank_records[count]
    print(list)
    print("Welcome {0}. Thank you for joining {1}. Your balance is ${2}.\n"
          .format(list_1[0],list_1[1],list_1[2]))

'''
#assertion5
input: bank_records = [["Amy","ANZ", 10000],["JK","ASB",39999],["Brody","KIWI Bank",10900]]
output:
<class 'list'>
Welcome Amy. Thank you for joining ANZ. Your balance is $10000.

<class 'list'>
Welcome JK. Thank you for joining ASB. Your balance is $39999.

<class 'list'>
Welcome Brody. Thank you for joining KIWI Bank. Your balance is $10900.

