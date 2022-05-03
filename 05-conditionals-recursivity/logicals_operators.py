operator_and = 2 + 2 == 4 and 3 + 1 == 4 # True

operator_or = 8 % 2 == 0 or 8 % 3 == 0 # True

operator_not = not (8 > 6) # False


for result in [operator_and, operator_or, operator_not]:
    print(result, end=' ')
