a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

print("first number before swap: ",a)
print("second number before swap: ",b)

a,b = b,a
print("first number after swap: ",a)
print("second number after swap: ",b)