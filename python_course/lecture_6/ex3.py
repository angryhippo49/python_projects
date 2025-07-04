x=37

got_it=False
for i in range (5):
    num=eval(input("Guess the number between 1 and 100: "))
    if num>x:
        print("Too high!")
    if num<x:
        print("Too low!")
    if num==x:
        print("Correct! You guessed the number in", i+1, "attempts.")
        got_it=True
        break

if not got_it:
    print("dumbo")