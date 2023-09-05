year=int(input("enter the year"))
if year%4==0:
    print("it is a leap year")
elif year<0000 or year>9999:
    print("invalid input")
else:
    print("not a leap year")