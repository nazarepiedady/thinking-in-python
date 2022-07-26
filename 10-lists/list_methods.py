alphabet_letters = ['a', 'b', 'c']
alphabet_letters.append('d')
print(alphabet_letters)

alphabet_letters = ['a', 'b', 'c']
more_alphabet_letters = ['d', 'e']
alphabet_letters.extend(more_alphabet_letters)
print(alphabet_letters)

unordered_alphabet_letters = ['d', 'c', 'e', 'b', 'a']
unordered_alphabet_letters.sort()
print(unordered_alphabet_letters)


alphabet_letters = ['a', 'b', 'c', 'd', 'e']
alphabet_letters.pop(1)
alphabet_letters.pop()
print(alphabet_letters)
