alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z'," "]

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text,shift_amount):
    cipher_text =""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position +shift_amount
        if new_position > 26:
            new_position2 = new_position-27
            new_letter2 = alphabet[new_position2]
            cipher_text += new_letter2
        else:
            new_letter1 = alphabet[new_position]
            cipher_text += new_letter1
    print(f"The encoded text is {cipher_text}.")
encrypt(plain_text = text,shift_amount = shift)