# Create a class for the principal and interest
class Investments:

    # constructor
    def __init__(self, p: float, i: float) -> None:
        self.p = p
        self.i = i

    # create a method to find the investmen value after n years
    def value_after(self, n: float) -> float:
        investment = self.p * ((1 + self.i)**n)
        print(f'Principle - ${self.p}, interest rate - {self.i}% Money after {n} years - ${investment}')
        return investment


# main function
if __name__ == "__main__":
    principal = eval(input("What is the principal? "))
    interestrate = eval(input("What is the interest rate? "))
    time = eval(input("How many👌 years? "))
    house = Investments(principal, interestrate)
    print(house.value_after(time))