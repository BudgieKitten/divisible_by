"""
Pre: number must be an integer with type string
"""
def divisible_by_4(number):
    numbers_divisible_by_4 = [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40]

    last_2_digits = number[-2]

