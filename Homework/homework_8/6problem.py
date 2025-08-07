# imports
from random import randint

# Create a list to put the lottory numbers into
lotto=[]

#Create a loop to generate the lotto numbers
for i in range(6):
    lotto+=[randint(1,48)]

# print the winning lotto numbers
print("The winning lotto numbers are ",lotto)