# Get list from user
my_list = eval(input("Enter a list: "))

# Save last element
temp = my_list[-1]

# Switch every element with the one before it
for i in range(len(my_list)-1,-1,-1):
    my_list[i]=my_list[i-1]

# Replace first element with original last element
my_list[0]=temp

# Print new list
print(my_list)