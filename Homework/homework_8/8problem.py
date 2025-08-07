from random import randint
hat=[]
num=eval(input("How many people are here: "))
for i in range(1,num+1):
    entries=eval(input("How many entries does this person get: "))
    for x in range(entries):
        f="person",i
        hat+=[f]
print(hat[randint(0,len(hat))])