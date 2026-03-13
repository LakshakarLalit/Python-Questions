year = int(input("Enter a year: "))

if ((year%400==0) and (year%100==0)):
    print("This year is leap year")
else:
    print("This year is not leap year")