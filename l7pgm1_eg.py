file_path = input("Enter the file path: ")
lines = []
with open(file_path, 'r') as file:    
    for line in file:
        lines.append(line.strip())
print(lines)
