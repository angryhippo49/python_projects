x=eval(input("Enter the amount of elements: "))
z=eval(input("Enter a threshold: "))
sum=0
for i in range(x):
    y=eval(input("Enter a number: "))
    if y>z:
        sum=sum+1
print("there are ", sum, "numbers greater than", z)