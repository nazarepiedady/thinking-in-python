def compare_two_values(first_value, second_value):
    if first_value > second_value:
        return 1
    elif first_value == second_value:
        return 0
    else:
        return -1


two_bigger_than_one = compare_two_values(2, 1)
two_is_equal_two = compare_two_values(2, 2)
two_smaller_than_three = compare_two_values(2, 3)

for result in [two_bigger_than_one, two_is_equal_two,
                two_smaller_than_three]:
    print(result, end=' ')
