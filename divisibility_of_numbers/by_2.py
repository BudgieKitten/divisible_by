"""
Pre: number must be an integer with type string
"""
def divisible_by_2(number):
    numbers_divisible_by_2 = [0, 2, 4, 6, 8]

    last_digit = number[-1]

    return int(last_digit) in numbers_divisible_by_2