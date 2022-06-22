def is_abecedarian_loop(word):
    previous = word[0]
    for char in word:
        if char < previous:
            return False
        previous = char
    return True


def is_abecedarian_recursive(word):
    if len(word) <= 1:
        return True
    if word[0] > word[1]:
        return False
    return is_abecedarian_recursive(word[1:])
