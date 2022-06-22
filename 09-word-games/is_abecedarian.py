def is_abecedarian(word):
    previous = word[0]
    for char in word:
        if char < previous:
            return False
        previous = char
    return True
