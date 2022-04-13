def print_twice(value):
    for time in range(2):
        print(value)

def cat_twice(first_part, second_part):
    cat = first_part + second_part
    print_twice(cat)

cat_twice('Bing tiddle ', 'tiddle bang.')
