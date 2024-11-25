# main.py

import Armstrong

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

armstrong_numbers = Armstrong.generate_armstrong_numbers(start, end)

print(f"Armstrong numbers between {start} and {end}:")
print(armstrong_numbers)

