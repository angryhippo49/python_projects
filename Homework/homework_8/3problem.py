# Imports
from random import randint

# Ask user for a sentence
text = input("Enter a sentence: ")
words = text.split()

# Create a new list to store randomized elements
new_list = []
# random index loop
new_list = []
for i in range(len(words)):

    # create a temporary variable to store the random word
    temp=words[randint(0,len(words)-1)]

    # add that random word to the new list
    new_list+=[temp]

    # remove the random word from the origional list to prevent repetition
    words.remove(temp)

# Create new string for sentence of shuffled words
new_string = ""

# list to sentence loop
for i in range (len(new_list)):

    # add each word of the shuffled list to the empty string plus a space
    new_string+= new_list[i]+" "

# print out the shuffled sentence
print(new_string)