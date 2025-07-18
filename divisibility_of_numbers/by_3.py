"""
Pre: number must be an integer with type string
"""
def divisible_by_3(number):
    numbers_divisible_by_3 = [3, 6, 9]

    if len(number) == 1:
        return int(number) in numbers_divisible_by_3

    sum_of_all_characters = 0

    for i in number:
        sum_of_all_characters += int(i)

    return divisible_by_3(str(sum_of_all_characters))