from random import randint
x=[]
f=0
for i in range(20):
    i=randint(1,100)
    x=x+[i]
print(x)
for i in x:
    if x[0]==i:
        y=i
        z=i
        s=i
    else:
        y=y+i
    if i<z:
        z=i
    if i>s:
        s=i
    if i%2==0:
        f+=1
print(y/20)
print("The largest and smallest are",s,"and",z,".")
print("There are",f,"even numbers.")