x=eval(input("Enter a list of numbers from 1 to 12: "))
for i in range(len(x)):
    if(x[i]>10):
        x[i]=10
print(x)