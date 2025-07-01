x=eval(input("Enter a positive integer: "))
if x==0:
    print("The factorial of 0 is 1.")
else:
    facts=1
    for i in range(x,0, -1):
        facts=facts*i
    print("the factorial of ", x,"is", facts)