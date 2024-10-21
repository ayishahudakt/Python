words=input("enter words separated by spaces:").split()
max_length=0
for word in words:
    current_length=0
    for char in word:
        current_length +=1
    if current_length > max_length:
        max_length=current_length
print("length of the longest word:",max_length)
