# imports
from random import randint

# Create a list to put the lottory numbers, amount of draws to get them, and the draws into
lotto=[]
numofdraws=[]
draw=[]
# Create a loop to generate the lotto numbers
for i in range(6):
    lotto+=[randint(1,10)]

# run a loop 1000 times to simulate a drawing
for i in range(1000):

    # count how long it took to get the lotto
    if draw==lotto:
        numofdraws+=[i+1]

    # reset the draw
    draw=[]
    for x in range(6):

        #s imulate draw
        draw+=[randint(1,10)]
print("The average number of drawings needed to win the lotto is",sum(numofdraws)/1000)