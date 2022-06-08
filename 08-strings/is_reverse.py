def is_reverse(first_word, second_word):
    if len(first_word) != len(second_word):
        return False
    first_word_index = 0
    second_word_index = len(second_word) - 1
    while second_word_index >= 0:
        if first_word[first_word_index] != second_word[second_word_index]:
            return False
        first_word_index = first_word_index + 1
        second_word_index = second_word_index - 1
    return True
