# imports
from typing import List

# function for closest element
def closest_to_n(L: List, n: int) -> int:
    closest = -9999
    for x in L:
        if x <= n:
            if x > closest:
                closest = x
    return closest



# main function
if __name__ == "__main__":
    L = eval(input("Enter a list: "))
    n = eval(input("Enter the number you want to find the closest to: "))
    answer = closest_to_n(L, n)
    print(answer)