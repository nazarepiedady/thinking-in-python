def get_absolute_value(number):
    if number < 0:
        return -number
    else:
        return number


positive_absolute_value = get_absolute_value(10)
negative_absolute_value = get_absolute_value(-5)

print(positive_absolute_value, negative_absolute_value)
