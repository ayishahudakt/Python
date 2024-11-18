n = int(input("Enter the number of powers of 2 to display: "))

numbers = list(range(n))

# Use map with a lambda function to calculate 2 raised to the power of each number
powers_of_2 = map(lambda x: 2 ** x, numbers)

print("Powers of 2:", list(powers_of_2))

