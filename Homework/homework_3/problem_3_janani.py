x = eval(input("Enter a number: "))

if x % 2 == 0:
    print(x, "is even ", end='')
    if 10 <= x <= 50:
        print("and within range")
    else:
        print("and outside range")
else:
    print(x, "is odd ", end='')
    if 10 <= x <= 50:
        print("and within range")
    else:
        print("and outside range")