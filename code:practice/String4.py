# String4.py
#
# @ author: Amy
# date: 11.11.22

string_1 = "Hello World"

print(string_1.replace("Hello", "Goodbye"))
string_2 = "hElLo wOrlD"
print(string_2.upper())
print(string_2.lower())
print(string_2.title())
print(string_2.capitalize())
print(string_2.swapcase())
print("*".join(reversed(string_2)))

string_3 = "  xyzx  "
print("Original string is.... \n")
print("***",string_3,"***\n")
print("Using strip()...\n")
print("***",string_3.strip("x"),"***\n")
print("Using lstrip()...\n")
print("***",string_3.lstrip("x"),"***\n")
print("Using lstrip()...\n")
print("***",string_3.rstrip("x"),"***\n")
