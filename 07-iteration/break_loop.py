def get_user_input():
    while True:
        value_inputed = input('> ')
        if value_inputed.lower() == 'done':
            break
        print(value_inputed)
    print('Done!')
