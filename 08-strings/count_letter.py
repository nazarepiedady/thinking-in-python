def count_letter(word='banana'):
    count = 0
    for letter in word:
        if letter == 'a':
            count = count + 1
    return count
