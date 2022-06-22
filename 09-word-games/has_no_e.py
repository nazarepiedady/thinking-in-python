def has_no_e(word):
    if isinstance(word, str):
        for char in word:
            if char == 'e':
                return True
        return False
    raise TypeError(f'{word} should be a str')
