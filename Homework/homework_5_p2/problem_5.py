x=eval(input("Enter the amount of elements: "))
sum=0
for i in range(x):
    y=eval(input("Enter a number: "))
    sum=sum+y
print("The average is", sum/x)