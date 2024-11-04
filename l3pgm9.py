n=int(input("enter a program to check if it is an armstrong number:"))
original_n=n
sum=0

while n>0:
    digit=n%10
    sum+=digit**3
    n=n//10

if sum==original_n:
    print(original_n,"is an armstrong no")
else:
    print(original_n,"not an armstrong no")

