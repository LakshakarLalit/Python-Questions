purchase=float(input("Enter purchase amount: "))
discount = 0

if purchase>=5000:
    discount=(purchase*10)/100

total = purchase - discount

print("Total amount: ",total)