# create a function for the factorial

def factorial(n: int) -> int:

    # create a variable to multiply the digits
    product = 1

    # loop for factorial
    for i in range(n):
        product = product*(n-i)

    return product



# function for binomial coefficient
def binom(n: int, k: int) -> int:
    nchoosek = (factorial(n))/((factorial(k))*(factorial(n-k)))
    return nchoosek

# ask user for integers to binom
n = eval(input("Enter the thing you want to make other things with: "))
k = eval(input("enter the thing you want made: "))

# use the functions and print the answer
answer = binom(n,k)
print(answer)