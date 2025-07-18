"""
Pre: number must be an integer with type string
"""
def divisible_by_5(number):
    numbers_divisible_by_5 = [0, 5]

    last_digit = int(number[-1])

    return last_digit in numbers_divisible_by_5