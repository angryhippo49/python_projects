x=eval(input('Enter a positive'))
flag =0
for i in range(x):
    if x%i==0:
        flag=1
if flag==1:
    print("not prime")
else:
    print("prime")
    for y in range(x):
        if y%i==0:
            pass
        else:
            print("Prime numbers up to", x)