age=int(input("Enter your age: "))

if age>18:
    print("You can vote")
elif age<18 and age>0:
    print("you cannot vote")
else: 
    print("not valid")