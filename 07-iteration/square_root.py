def calculate_square_root(x, a):
    while True:
        print(x)
        y = (x + a / x) / 2
        if y == x:
            break
        x = y
