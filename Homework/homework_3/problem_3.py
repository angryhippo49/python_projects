x=eval(input("enter a number: "))
if (x%2==0) and (10<=x<=50): 
    print(x, "is even and within the range of 10 and 50")
elif (10<=x<=50):
    print(x, "is odd and within the range")
elif (x%2==0):
    print(x, "is even but is not within the range")
else:
    print(x, "is odd and not within the range")