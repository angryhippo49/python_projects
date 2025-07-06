# Create a place to store the dictionary and the keys
productprice = []
productname = []

#Create a variable for an infinite loop
condition = True

# Create a loop that will store the price and corresponding product name in two different lists
for i in range(9999):
    
    name=input("Enter a product name or enter 'done' when finished: ")
    # Have a way to break out of the loop
    if name == "done":
        break
    else:

        # add the product name and price to the lists
        productname+=[name]
        price=eval(input("Enter a price: "))
        productprice+=[price]

while condition==True:
    key=input("Enter a name of one of your products: ")
    if productname.count(key) == 0:
        print("This product doesn't exist")
    else:
        index=productname.index(key)
        print("The price for ",productname[index],"is $",productprice[index])
