# Create a place to store the dictionary and the keys
productprice = []
productname = []

#Create a variable for an infinite loop
condition = True

# Create a loop that will store the price and corresponding product name in two different lists
for i in range(99999):
    
    input=input("Enter a product name or enter 'done' when finished: ")

    # Have a way to break out of the loop
    if input == "done":
        break
    else:

        # add the product name and price to the lists
        productname+=input
        productprice+=eval(input("Enter a price: "))
while condition==True:
    key=input("Enter a name of one of your products: ")
    index=productname.index(key)
    print("The price for ",productname[index],"is $",productprice[index])