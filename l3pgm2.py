def fibonacci_series(n):
    fib_series=[]
    a,b=0,1
    for _ in range(n):
        fib_series.append(a)
        a,b =b,a+b
    return fib_series

n_terms=int(input("enter the no.of terms for the fibonacci series:"))
print("fibonacci series of ",n_terms, "terms:",fibonacci_series(n_terms))
