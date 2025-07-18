"""
Pre: number must be an integer with type string
"""
def divisible_by_8(number):
    numbers_divisible_by_8 = [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40]

    last_3_digits = int(number[-2:]) % 40
