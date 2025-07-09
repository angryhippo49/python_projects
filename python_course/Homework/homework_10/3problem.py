# create a function to add the digits of an integer
def sum_digits(x:int)->int:
    # create a variable to add the digits to
    sum = 0

    # loop for digit adding
    while x > 0:
        digit = x%10
        sum += digit
        # x reduces by 1/10th each time
        x = int(x/10)

    return sum


if __name__ == '__main__':
    num = eval(input("Enter a number: "))
    num = sum_digits(num)
    print("The digits added up are ",num)