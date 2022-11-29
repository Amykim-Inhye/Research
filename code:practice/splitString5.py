# splittingStrings5.py
#
# @ author: Amy
# date:12.11.22
eng_dict = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z']
user_input=input("Please enter the text that you wish to encrypt or decrypt, followed by a comma and the integer key.\n\n")

split_user_input = user_input.split(",")
#[learn],[9]
sentence = split_user_input[0]
offset = int(split_user_input[1])

def get_cipher(sentence,offset):
    result=""
#range(0,5)
    for count in range(0,len(sentence)):
        num = ord(sentence[count])
        num +=offset
        if num >ord('z'):
            num -=26
        elif num<ord('a'):
            num +=26
        
        letter = chr(num)
        result += letter
    return result

print(get_cipher(sentence, offset))
'''
sassertion9

input:learn,9
output:unjaw
