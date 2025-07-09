# Create a function that takes a list of strings, and adds a ! at the end.
from typing import List

# adds exclamation
def add_excitement(L: List) -> None:
    new_L=L[:]
    for i in range(len(new_L)):
        L[i] = new_L[i]+'!'
        
    
def change_variable(l: int) -> None:
    print("l inside function, before change: ", l) # 9
    l = l + 1
    print("l inside function, after change: ", l) # 10
    return

if __name__ == '__main__':
    # ask user for a list   
    # my_list=eval(input("Enter a list: "))

    # call add_excitement
    # add_excitement(my_list)
    # print(my_list)

    l = 9
    print("l before function call: ", l) # 9
    change_variable(l)
    print("l after function call: ", l) # 10