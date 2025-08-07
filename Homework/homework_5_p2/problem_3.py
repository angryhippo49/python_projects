x=eval(input("Enter a start: "))
y=eval(input("Enter an end: "))
count=0
for i in range(x, y+1):
    if i%2==0:
        count=count+1
print("there are", count, "even numbers between", x,"and", y)