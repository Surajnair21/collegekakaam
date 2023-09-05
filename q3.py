x=int(input("enter the value of x"))
y=int(input("enter the value of y"))
if x<0 or y<0:
    print("invalid input")
elif x%y==0:
    print("yes it is divisible")
else:
    print("not divisible")