# imports
from random import randint

# function for random digit
def random_digits_n(n: int) -> int:
    sum = 0
    for i in range(n):
        if i == 0:
            sum += randint(1,n)*(10**(n-1))
        else:
            sum += randint(0,n)*(10**(n-1))
        
        # reduces n by 1
        n -= 1
    return sum



# main function
if __name__ == "__main__":
    numofdigits = eval(input("Enter the amount of dgits: "))
    answer = random_digits_n(numofdigits)
    print(answer)