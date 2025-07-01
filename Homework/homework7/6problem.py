x=[]
y=[]
z=[]
for i in range(50):
    x+=[i]
for i in range(1,51):
    y+=[i**2]
for i in range(26):
    z+=[chr(97 + i) * (i + 1)]
print(x,y,z)