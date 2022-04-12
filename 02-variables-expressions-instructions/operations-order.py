# mathematic operations order

parenthesis_first = 2 * (3 - 1) # 4

exponential_first = 1 + (2 ** 3) # 9

multiplication_first = 2 * 3 - 1 # 5

division_first = 6 + 4 / 2 # 8

addition_first = 1 + 3 - 2 # 2

subtration_first = 6 - 5 + 1 # 2

# iterate through over resulted value list
for result in [parenthesis_first, exponential_first, multiplication_first,
              division_first, addition_first, subtration_first]:
    print(result)
