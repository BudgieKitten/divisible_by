from by_2 import divisible_by_2 as div2
from by_3 import divisible_by_3 as div3

"""
Pre: number must be an integer with type string
"""
def divisible_by_6(number):
    # If number is divisible by both 2 and 3
    return div2(number) and div3(number)