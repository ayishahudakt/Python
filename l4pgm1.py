def calc_intr(principal,time,is_senior):
    rate =12 if is_senior else 10

    interest=(principal * rate * time)/100
    return interest

principal=float(input("enter the principal amount:"))
time=float(input("enter the time (in years):"))
is_senior=input("is the customer a senior citizen?(Y/N):").strip().lower()=="y"
interest=calc_intr(principal,time,is_senior)
print("the calculated interest is",interest)
