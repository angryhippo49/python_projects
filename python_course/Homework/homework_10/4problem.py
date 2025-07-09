# create a function to add the digits of an integer
def digital_root(x:int)->int:
    
    while x >= 10:
        # create a variable to add the digits to
        sum = 0
        # loop for digit adding
        while x > 0:
            digit = x%10
            sum += digit
            # x reduces by 1/10th each time
            x = int(x/10)
        x=sum
    return x



if __name__ == '__main__':
    num = eval(input("Enter a number: "))
    num = digital_root(num)
    print("The digital root is ",num)