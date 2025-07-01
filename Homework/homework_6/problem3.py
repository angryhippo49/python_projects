s= input("Enter a string: ")
alphabet="abcdefghijklmnopqrstuvwuxyz"
numeric="0123456789"
x=0
for i in s:
    if (i in alphabet):
        continue
    else:
        if(i in numeric):
            x=1
        else:
            x=2
            print("This string contains special characters.")
            break
if(x==1):
    print("This string is alphanumeric.")
elif(x==0):
    print("This string contains only alphabets!")