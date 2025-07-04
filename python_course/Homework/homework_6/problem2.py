s= input("Enter a string: ")
x= ""
for i in range(len(s)):
    if s[i]!=" ":
        x=x+s[i]
print("String with no spaces: ",x)