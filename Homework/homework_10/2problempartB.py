# Create a function that takes a list of strings, and adds a ! at the end.
from typing import List

# create an empty list to put the updated strings into
new_list=[]

# adds exclamation
def add_excitement(L: List) -> None:
    for i in range(len(L)):
        new_list.append(L[i]+"!")
    return new_list
        
    


if __name__ == '__main__':
    # ask user for a list   
    my_list=eval(input("Enter a list: "))

    # call add_excitement
    my_list=add_excitement(my_list)
    print(my_list)
