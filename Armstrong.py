# Armstrong.py

def is_armstrong(num):
    digits = str(num)
    power = len(digits)
    sum_of_powers = sum(int(digit) ** power for digit in digits)
    return sum_of_powers == num

def generate_armstrong_numbers(start, end):
    return [num for num in range(start, end + 1) if is_armstrong(num)]


