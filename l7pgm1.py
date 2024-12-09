file_path = input("Enter the file name: ")

lines = []

try:
    with open(file_path, 'r') as file:
        for line in file:
            lines.append(line.strip())

    print("Lines from the file:")
    print(lines)

except FileNotFoundError:
    print(f"The file at {file_path} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

