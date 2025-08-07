# imports
from random import randint

# initialize variables
list_of_outcomes=[]

# generate random outcomes 10K times
# and append to list
for i in range(10000):
    random_outcome=randint(1,6)+randint(1,6)
    list_of_outcomes+=[random_outcome]

# calcuate statistics and print
for possible_outcome in range(2,13):
    ct=list_of_outcomes.count(possible_outcome)
    print(possible_outcome,ct/10000*100)