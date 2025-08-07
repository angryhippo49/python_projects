# Create a function to return the list of a number's factors
def factors_of_n(x: int) -> int:
    listoffactors = []
    for i in range(1,x+1):
        if x%i == 0:
            if x/i not in listoffactors:
                listoffactors += [  i,x/i]
    return listoffactors


# main function
if __name__ == "__main__":
    num = eval(input("Enter a number: "))
    print(factors_of_n(num))