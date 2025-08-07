x=input("Enter the base character: ")
rep=eval(input("Enter the number of repetitions per line: "))
lines=eval(input("Enter the number of lines: "))
for i in range (lines):
    print(rep*x)
    rep=rep+1