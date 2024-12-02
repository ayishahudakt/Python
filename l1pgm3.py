import calendar

# Get the current year
current_year = 2024  # Or you can use: current_year = datetime.datetime.now().year

# Get the final year from the user
final_year = int(input("Enter the final year: "))

# List to store leap years
leap_years = []

# Loop through each year from current year to final year
for year in range(current_year, final_year + 1):
    if calendar.isleap(year):  # Check if the year is a leap year
        leap_years.append(year)

# Display the leap years
print(f"Leap years from {current_year} to {final_year}:")
for year in leap_years:
    print(year)

