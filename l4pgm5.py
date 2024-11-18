def add_numbers(*args):
    return sum(args)

user_input = input("Enter integers separated by space: ")
input_list = []
numbers=map(int, user_input.split())

result = add_numbers(*numbers)
print("the sum is:",result)
