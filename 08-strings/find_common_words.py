def find_common_words(first_word='', second_word=''):
    for letter in first_word:
        if letter in second_word:
            print(letter)
