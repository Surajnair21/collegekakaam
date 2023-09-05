r=int(input("enter the radius"))
if r<1 or r>100:
    print("invalid input")
else:
    area=3.14*r*r
    print("the area is ",area)