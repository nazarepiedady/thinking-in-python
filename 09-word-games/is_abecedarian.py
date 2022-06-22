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


def is_abecedarian_while(word):
    index = 0
    while index < len(word)-1:
        if word[index+1] < word[index]:
            return False
        index = index + 1
    return True
