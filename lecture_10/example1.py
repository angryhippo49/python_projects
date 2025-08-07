i = 1000

from typing import List, Tuple

def product_price_code():
    # make a dictionary for products and prices
    d={}

    # make a condition for an infinite loop
    condition=True

    # loop
    for i in range(1000):
        name=input("Enter a product name or done to end: ")
        if name=='done':
            break
        price=eval(input("Enter a price: "))
        d[name]=price
    while condition==True:
        key=input('What product are you looking for or are you looking for a price? ')
        if key=='a price' or key == 'price':
            budget=eval(input('What price are you looking for: '))
            for i in d:
                if d[i]<budget:
                    print(i)
        elif key not in d:
            print("We're out of stock with that sorry")
        else:
            print(d[key])
    print(i)


# function to compute the summation of N
# summation_N = 1 + 2 + 3 + 4 + .... + N
# def function_name(variable_name1: variable_type1, variable_name2: variable_type2) -> 
def summation_N(N: int) -> Tuple[int, int]:
    total = 0
    for i in range(1, N+1):
        total += i
    return total, N