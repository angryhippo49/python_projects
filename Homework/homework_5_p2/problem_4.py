x=eval(input("Enter the amount of elements: "))
for i in range(x):
    y=eval(input("Enter a number: "))
    if i==0:
        min=y
        max=y
    else:
        if y<min:
            min=y
        if y>max:
            max=y
print(min)
print(max)