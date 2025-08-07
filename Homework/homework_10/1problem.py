def rectangle(m:int, n:int) -> None:
    for i in range(m):
        print("*"*n)

height=eval(input("Enter a height: "))
width=eval(input("Enter a width: "))

rectangle(height,width)