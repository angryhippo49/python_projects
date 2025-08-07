# An example demonstrating the break statement
# Ask user to enter 10 non-negative numbers.
# If all inputs are valid, then good.
# However, if they enter any invalid inputs, then just quit the loop.

print("Enter 10 numbers; all non-negative!")

count = 0
for i in range(10):
    x = eval(input(f"Enter the {i+1}th number: "))
    
    if x < 0:
        print("You entered an invalid input! Try next time!")
        break
    else:
        count += 1 # same as count = count + 1

if count == 10:
    print("Yay, you are all good!")