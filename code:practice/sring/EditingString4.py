#EditingString4 .py
#
# @ author: Amy
# date: 11.11.22

sentence = "The only thing that scares me is Keyser Soze."
sentence = sentence.replace(" ","*")
print(sentence)
sentence = sentence.lower()

new_sentence = ""

for cha in range(0, len(sentence)):
    if cha %5 ==0:
        letter = sentence[cha]
        letter = letter.upper()
        new_sentence += letter
    else:
        new_sentence += sentence[cha]
print(new_sentence)

'''
#assertion6

input: sentence = "The only thing that scares me is Keyser Soze."
output: The*only*thing*that*scares*me*is*Keyser*Soze.
The*oNly*tHing*That*ScareS*me*Is*keYser*Soze.
