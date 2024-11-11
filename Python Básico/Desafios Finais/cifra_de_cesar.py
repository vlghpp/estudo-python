vowels_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
vowels_lower = 'abcdefghijklmnopqrstuvwxyz'

text = "Cachorro!"
key = -1

def encrypt(string: str, key: int) -> str:
    new_string = ""
    for letter in string:
        if letter.isupper():
            index_letter = vowels_upper.find(letter)
            if index_letter == -1:
                new_string += letter
            else:
                new_index = (index_letter + key) % len(vowels_upper)
                new_string += vowels_upper[new_index]

        elif letter.islower():
            index_letter = vowels_lower.find(letter)
            if index_letter == -1:
                new_string += letter
            else:
                new_index = (index_letter + key) % len(vowels_lower)
                new_string += vowels_lower[new_index]

        else:
            new_string += letter

    return new_string

print(encrypt(text, key))
