x=eval(input("enter a side: "))
y=eval(input("enter a side: "))
z=eval(input("enter a side: "))
if x+y>z and x+z>y and y+z>x:
    if x==y and y==z:
        print("this is equilateral")
    elif x==y or x==z or y==z:
        print("this isoscoles")
    else:
        print("this is scalene")
else:
    print("this ain't right")