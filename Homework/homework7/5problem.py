x=eval(input("Enter a list of strings: "))
y=[]
for i in range(len(x)):
    y+=[x[i][1:]]
print(y)