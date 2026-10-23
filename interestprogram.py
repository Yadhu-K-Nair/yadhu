principle=float(input("enter the amount: "))
interest=float(input("enter the interst rate: "))
time=float(input("enter the number of year: "))
simpleinterest=principle*interest*time/100
finalamount=principle+simpleinterest
print("SimpleInterest= ",simpleinterest)
print("Amount= ",finalamount)