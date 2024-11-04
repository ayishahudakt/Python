def sum_of_list(lst):
    total=0
    for item in lst:
        total += item
    return total

user_inp=input("enter numbers seprated by spaces:")
num=list(map(int, user_inp.split()))
print("sum of the list",sum_of_list(num))
