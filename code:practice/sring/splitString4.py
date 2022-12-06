# splittingStrings4.py
#
# @ author: Amy
# date:12.11.22

fruits ="Orange, Apple, Banana, Watermelon, Grape"

split_word = fruits.split(", ")
print(split_word)

unique_list = set(split_word)
print(unique_list)
'''
assertion7
input:fruits ="Orange, Apple, Banana, Watermelon, Grape"

output:{'Banana', 'Grape', 'Watermelon', 'Orange', 'Apple'}
