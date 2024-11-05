def cmp_string(s1,s2,n):
    return s1[:n]==s2[:n]

s1=input("enter the first string:")
s2=input("enter the second string:")
n=int(input("enter a number to compare the string:`"))

result=cmp_string(s1,s2,n)
print("the result is",result)
