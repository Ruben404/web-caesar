import string


def alphabet_position(character):
    alphabet = string.ascii_lowercase
    lower = character.lower()
    return alphabet.index(lower)

def rotate_string_13(text, num):

    rotated = ''
    alphabet = string.ascii_lowercase

    for char in text:
        
        if char.isalpha():

            rotated_idx = ((alphabet_position(char) + int(num)) % 26)

            if char.isupper():
                rotated += alphabet[rotated_idx].upper()
            else:
                rotated += alphabet[rotated_idx]
        
        else:
            rotated += char

    # print(rotated)
    return rotated


