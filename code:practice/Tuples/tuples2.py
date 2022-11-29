#Tuples2.py
#author:amy
#date:08.11.22

bank_accounts = (("Joe",33,"234 Great southroad", "022629107"),
                 ("Tama", 6000),
                 ("Suzanne",21025, "45 Green Lane"),
                 ("Anihera",-75))

print(len(bank_accounts))

for i in bank_accounts:
    print("\nThe name is ", i[0],"and the balance is $",i[1])

for i in bank_accounts:
    if len(i) >2:
        print("\nThe name is",i[0], "and the address is",i[2])

low_balance = 100

for i in bank_accounts:
    if i[1] < low_balance:
        print("\nA customer with less than ${0} is {1}".format(low_balance,i[0]))

for i in bank_accounts:
    if len(i) <=2:
        print("\nA customer with either no number or address is",i[0])


balances_list = []
for i in bank_accounts:
    balances_list.append(i[1])

    print("\nThe highest balance is ${0}.".format(max(balances_list)))
    print("\nThe lowerest balance is ${0}.".format(min(balances_list)))
    print("\nThe sum balance is ${0}".format(sum(balances_list)))

print("\nShowing details for all customer...")
for i in bank_accounts:
    print("\n")
    for customer_detail in i:
        print(customer_detail, end = ",")

print("\n\nShowing details for our rich and poor customer...", end="")
for i in bank_accounts:
    if 0>i[1] or i[1]>5000:
        print("\n")
        for customer_detail in i:
            print(customer_detail, end="")
              
