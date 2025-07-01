x=[8,9,10]
x[1]=17
x=x+[4,5,6]
x.remove(x[0])
x.sort()
x=x*2
x=x[:3]+[25]+x[3:]
print(x)