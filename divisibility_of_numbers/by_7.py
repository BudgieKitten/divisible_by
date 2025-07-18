"""
Pre: number must be an integer with type string
"""
def divisible_by_7(number):
    # Only 0 and 7 divisible by 7
    if len(number) == 1:
        return int(number) % 7 == 0

    # Take the last digit, multiply by 2, then take the remaining digits and subtract it with this digit
    # Source: https://www.grayson.edu/current-students/academic-resources/student-labs/math-hub-pdfs/Divisibility%20Rules.pdf
    # Source: https://en.wikipedia.org/wiki/Divisibility_rule#7
    last_digit = int(number[-1])
    subtraction = int(number[:-1]) - (last_digit * 2)

    # Only deal with positive numbers
    if subtraction < 0:
        subtraction = subtraction * -1

    return divisible_by_7(str(subtraction))