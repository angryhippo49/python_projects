
# Ask user to input a sentence
Text = input("Enter a sentence: ")

# Seperate each word and make them an element
words = Text.split()

#Print out the third word
print("The third word is: ",words[2])

for i in range (len(words)):
    if(i+1)%3==0:
        print(words[i])