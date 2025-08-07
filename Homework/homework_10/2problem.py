# Create a function that takes a list of strings, and adds a ! at the end.
from typing import List

# adds exclamation
def add_excitement(L: List) -> None:
    new_L=L[:]
    for i in range(len(new_L)):
        L[i] = new_L[i]+'!'
        
    


if __name__ == '__main__':
    # ask user for a list   
    my_list=eval(input("Enter a list: "))

    # call add_excitement
    add_excitement(my_list)
    print(my_list)
