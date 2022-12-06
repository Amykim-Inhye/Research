# splittingStrings3.py
#
# @ author: Amy
# date:12.11.22

sentence ="It is raining outside right now."
split_sentence= sentence.split(" ")
print(split_sentence)

def get_longest_word(split_sentence):
    longest_word=""
    for count in range(0,len(split_sentence)):
        if len(split_sentence[count]) > len(longest_word):
            longest_word = split_sentence[count]
    return longest_word

print(get_longest_word(split_sentence))


'''
assertion5
input: sentence ="It is raining outside right now."
output: raining
