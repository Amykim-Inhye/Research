# SearchingStrings3.py
# Author:Amy
# date: 11.11.22

password=input("Please put your password:\n")
contain_alpha = False
contain_number = False
contain_upper = False

if len(password) < 8 :
    print("Password needs to contain at least 8 character.")
if any(cha.isalpha() for cha in password)==False:
    print("The password needs to contain at least one alphabetical character\n")
if any(cha.isdigit() for cha in password) == False:
    print("The password needs to contain at least on digit.")
if any(cha.isupper() for cha in password) == False:
    print("The password needs to contain at least one uppercase character")
    
'''
#assertions9
input : Please put your password:
amykim91
output: The password needs to contain at least one uppercase character
Amykim91
