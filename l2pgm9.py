str1=input("enter 1st string:")
str2=input("enter 2nd string:")
if len(str1)>=2 and len(str2)>=2:
    str3=str1[0]+str2[1]+str1[2:]+" "+str2[0]+str1[1]+str2[2:]
else:
    print("both string must have atleast 2 characters")
print(str3)
