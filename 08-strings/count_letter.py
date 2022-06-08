def count_letter(word='banana', received_letter='a'):
    count = 0
    for letter in word:
        if letter == received_letter:
            count = count + 1
    return count
