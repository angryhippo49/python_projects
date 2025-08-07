min=10000000
max=-9999

for i in range(100000):
    x=eval(input("Enter a number(-1 to stop): "))
    if x==-1:
        break
    if x> max:
        max=x
    elif x<min:
        min=x
print("The minimum number is", min,"and the maximum number is ",max)