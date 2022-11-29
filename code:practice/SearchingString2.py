# SearchingStrings2.py
# Author:Amy
# date: 11.11.22

#"robert.paulson@hotmail.com" produces the username "paulsonr"

email="robert.paulson@hotmail.com"
dot_index = email.find(".")
print(dot_index)
at_index = email.find("@")
print(at_index)

surname = email[dot_index+1:at_index]
print("User's surname is {0}.".format(surname))

'''                       
#assertion
Input: email = "robert.paulson@hotmail.com"
Output: User's surname is paulson.
'''
