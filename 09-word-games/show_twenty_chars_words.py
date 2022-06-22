file = open('words.txt')

list_of_words = file.readlines()

for word_item in list_of_words:
    word = word_item.strip()
    if len(word) > 20:
        print(word)
