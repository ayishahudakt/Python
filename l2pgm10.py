color_list1=input("enter color for color_list1(seprated by space):").split()
color_list2=input("enter color for color_list2(seprated by space):").split()
colors_not_in_list2=[]
for color in color_list1:
    if color not in color_list2:
        colors_not_in_list2.append(color)
print("colors form color_lisit1 not conrained in color_list2",colors_not_in_list2)
