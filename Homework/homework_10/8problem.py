# create. function for the number of factors
def number_of_factors(x: int) -> int:
    listoffactors = []
    for i in range(1,x+1):
        if x%i == 0:
            if listoffactors.count(x/i) == 0:
                listoffactors += [i]
    return len(listoffactors)


# main function
if __name__ == "__main__":
    num = eval(input("Enter an integer: "))
    answer = number_of_factors(num)
    print(answer)