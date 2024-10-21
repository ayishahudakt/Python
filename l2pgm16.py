integers=list(map(int,input("enter a list of integers (space separated):").split()))
n=int(input("enter a number n:"))
word=input("enter a word:")
pos_num=[num for num in integers if num>0]
sqr_num=[num**2 for num in range(n)]
vowels=[char for char  in word if char in 'aeiouAEIOU']
ord_values=[ord(char) for char in word]
print("positive numbers:",pos_num)
print("square numbers:",sqr_num)
print("vowels:",vowels)
print("ordinary values:",ord_values)

