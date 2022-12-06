# splittingStrings2.py
#
# @ author: Amy
# date:12.11.22

import random
sentence = "Welcome to Wellington, enjoy time"

split_sentence = sentence.split(" ")

print(split_sentence)

random.shuffle(split_sentence)
print(split_sentence)
'''
assertion3.
input :sentence = "Welcome to Wellington, enjoy time"
output:['Welcome', 'to', 'Wellington,', 'enjoy', 'time']
['to', 'enjoy', 'Wellington,', 'time', 'Welcome']
 
