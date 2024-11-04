n=int(input("enetr a number to find its factors:"))
i=1
print("factors of",n,"are:")
while i<=n:
    if n%i==0:
        print(i)
    i+=1
