# convert valid types values to `integer`
string_integer = int('32')
float_integer = int(3.9999)

# convert valid types values to `float`
integer_float = float(32)
string_float = float('3.14159')

# convert valid types values to `string`
integer_string = str(32)
float_string = str(3.14159)

# print results for integer conversion
print('Integer values: ')
for integer in [string_integer, float_integer]:
    print(integer, end=' ')


print('\n\nFloater values: ')
# print results for float conversion
for floater in [integer_float, string_float]:
    print(floater, end=' ')


print('\n\nString values: ')
# print results for string conversion
for string in [integer_string, float_string]:
    print(string, end=' ')

