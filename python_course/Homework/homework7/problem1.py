x=eval(input("Enter a list: "))
y=0
z=0
print("There are ",len(x)," items")
print("The last one is ", x[-1])
print("Backwards is: ",x[::-1])
if 5 in x:
    print("Yes")
else:
    print("No")
for i in x:
    if i == 5:
        y+=1
    if i>5:
        z+=1
print("There are ",y," fives.")
print(x[1:-1])
print("There are ",z,"integers less than five.")