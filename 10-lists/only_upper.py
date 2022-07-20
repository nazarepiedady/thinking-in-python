def only_upper(strings_list):
    resulted_strings_list = []
    for string in strings_list:
        if string.isupper():
            resulted_strings_list.append(string)
    return resulted_strings_list
