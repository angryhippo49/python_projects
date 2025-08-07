L=eval(input("Enter a list of integers: "))
M=eval(input("Enter a list of integers: "))
N=[]
m=0
for i in range(len(L)):
   m=L[i]+M[i]
   N+=[m] 
print(N)