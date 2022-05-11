def countdown(number):
    if number <= 0:
        print('Blastoff!')
    else:
        print(number)
        countdown(number - 1)


def show_content_ntimes(content, times):
    if times <= 0:
        return
    print(content)
    show_content_ntimes(content, times - 1)


#countdown(10)
show_content_ntimes('You are seeing me now', 6)
