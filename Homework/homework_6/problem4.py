s=input("Enter a string: ")
if(s==s[-1:0:-1]+s[:1]):
    print("This is a palindrome")
else:
    print("this is not a palindrome")