import string


def alphabet_position(character):
    alphabet = string.ascii_lowercase
    lower = character.lower()
    return alphabet.index(lower)


def rotate_string_13(text, num):

    rotated = ''
    alphabet = string.ascii_lowercase

    for char in text:
        
        rotated_idx = (alphabet_position(char) + int(num) % 26)
        if char.isupper():
            rotated += alphabet[rotated_idx].upper()
        else:
            rotated += alphabet[rotated_idx]

    # print(rotated)
    return rotated


