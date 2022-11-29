# Enrolments.py
# author: amy
# date: 1.11.22

from datetime import date

distance_from_school = 3
age_in_years = 13
has_residency = True
is_fee_foreign = False

print("This program work out eligibility for enrolment...\n")


print("The student's eligibility to enrol is ",
      distance_from_school<4
      and 10 < age_in_years < 18
      and has_residency
      or 10 < age_in_years < 18
      and is_fee_foreign)

print("The student waited for too long...\n")



year_of_birth = input("\nPlease enter your year of birth: ")
name = input("Please enter your name: ")

current_date = date.today()
current_year = current_date.year
print(current_year)

print("The result of your applocation is" ,
      str((current_year - int(year_of_birth) >= 21)
        and name != "Suzanne May"
        and name != "Wiremu Rangi"))
