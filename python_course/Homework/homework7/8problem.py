num = int(input("Enter an integer: "))

# Create an empty list to store factors
fact = []

# Loop from 1 to the number (inclusive)
for i in range(1,num+1):
    if num % i == 0:
        fact.append(i)

# Display the result
print(fact)