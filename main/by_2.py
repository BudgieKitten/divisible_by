"""
Pre: number must be an integer with type string
"""
def divisible_by_2(number):
    numbers_divisible_by_2 = [0, 2, 4, 6, 8]

    last_index = number[-1]

    if int(last_index) in numbers_divisible_by_2:
        return True
    else:
        return False