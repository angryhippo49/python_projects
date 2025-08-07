N=eval(input("Enter the number of elements: "))
secndmax=-10001
max=-10000
for i in range (N):
    x=eval(input(f"Enter number {i+1}: "))
    if x>max:
        secndmax=max
        max=x
    elif secndmax<x<max:
        secndmax=x
print(secndmax)