# String.py
# @ author:Amy
# date: 11.11.22

string_1 = "here is a translation: Haera mai ki konei means come here!"
print(len(string_1))

print("The number of times that k appear is {0}\n".format(string_1.count("k")))

konei_endindex = string_1.find("konei") + len("konei")

print(konei_endindex)

print("The end index position of konei is {0}\n".format(konei_endindex))


here_position = string_1.find("here", konei_endindex, len(string_1))
#string_1.find("here",41,58)
print("Looking for the string_1 here, anytime after konei...\n"
      "The string_1 here appears at index position..{0}".format(here_position))


