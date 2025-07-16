# create a class called product
class Product:

    # create a field that takes in the name, price, and amount
    def __init__(self, n: str, p: float, a: int) -> None:
        self.name = n
        self.price = p
        self.amount = a
    

    # create a field that gets the price for x products
    def get_price(self, num_items: int) -> float:
        self.num = num_items
        if self.num < 10:
            totalprice = self.num * self.price
            return totalprice
        elif num_items >= 10 and num_items <= 99:
            totalprice = 0.9 * self.num * self.price
            return totalprice
        else:
            totalprice = 0.8 * self.num * self.price
            return totalprice
        

    # create a field that updates the stock after a purchase
    def make_purchase(self) -> int:
        self.amount -= self.num
        return self.amount


# main function
if __name__ == '__main__':
    name= input("what is the name of your product? ")
    price = eval(input("what is the price?  "))
    amount = eval(input("What is the amount in stock? "))
    num_items = eval(input("How many do you want to buy? "))
    product1 = Product(n = name, p = price, a = amount)
    print(f'Your total price will be {product1.get_price(num_items = num_items)} and there are {product1.make_purchase()} {name}s left in stock')


    name= input("what is the name of your product? ")
    price = eval(input("what is the price?  "))
    amount = eval(input("What is the amount in stock? "))
    num_items = eval(input("How many do you want to buy? "))
    product2 = Product(n = name, p = price, a = amount)
    print(f'Your total price will be {product2.get_price(num_items = num_items)} and there are {product2.make_purchase()} {name}s left in stock')


    name= input("what is the name of your product? ")
    price = eval(input("what is the price?  "))
    amount = eval(input("What is the amount in stock? "))
    num_items = eval(input("How many do you want to buy? "))
    product3 = Product(n = name, p = price, a = amount)
    print(f'Your total price will be {product3.get_price(num_items = num_items)} and there are {product3.make_purchase()} {name}s left in stock')