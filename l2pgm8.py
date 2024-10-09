inp_string=input("enter a string")
first_char=inp_string[0]
result=""
for index in range(len(inp_string)):
    if inp_string[index]==first_char and index!=0:
        result+="$"
    else:
         result+=inp_string[index]
print (result)
