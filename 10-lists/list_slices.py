alphabet_letters = ['a', 'b', 'c', 'd', 'e', 'f']

# start on the second to third
second_third_letters = alphabet_letters[1:3]
# slice the first four elements
first_four_letters = alphabet_letters[:4]
# slice from third index element to the end
from_third_letters = alphabet_letters[3:]
# make a copy of the previous list
alphabet_letters_copy = alphabet_letters[:]


print(
    second_third_letters, first_four_letters,
    from_third_letters, alphabet_letters_copy
)
