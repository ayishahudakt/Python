def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

def print_fib_series(n):
    for i in range(n):
        print(fibonacci(i), end="")

n=int(input("enter the no.of terms of the fibonacci series:"))
print("the fibonacci series are")
print_fib_series(n)
