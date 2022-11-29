#Challenge3.py
# @ author: amy
# 2. 11. 22

phone_plan = 15
add_airtime = 0.25
add_text = 0.15
support_cost = 0.44

user_airtime = int(input("please put how long use air time\n\n"))

user_text = int(input(" Please put how many text do you send?\n\n"))

if user_airtime<= 50 and user_text<=50:
    total_basic=int(phone_plan + support_cost)
    total_basic_tax = total_basic * 0.05
    print(total_basic+total_basic_tax)
    


if user_airtime >50 and user_text>50:
    total = int(((user_airtime - 50)*add_airtime)+((user_text - 50)*add_text)+phone_plan+ support_cost)
    total_tax = total* 0.05
    print(total + total_tax)
