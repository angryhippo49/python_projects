# create a function that returns the first location where two strings differ

def first_diff(string1:str,string2:str)->int:
    if string1 == string2:
        return -1
    elif len(string1) > len(string2):
        return divergence_index(string2, string1)
    else:
        return divergence_index(string1, string2)


def divergence_index(shortstring: str, longstring: str) -> int:
    """
    function returns first index of difference.
    """
    for i in range(len(shortstring)):
            if longstring[i] != shortstring[i]:
                return i
    return len(shortstring)


if __name__ == '__main__':
    s1 = input("Enter a string: ")
    s2 = input("Enter another string: ")

    print("difference is: ", first_diff(s1, s2))
