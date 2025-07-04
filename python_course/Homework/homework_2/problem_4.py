x=eval(input("enter a temperature: "))
y= input("Celsius or Farenheit(C or F): ")
if(y=="C"): print(x,"Celsius is equal to", x*1.8+32,"Farenheit")
if(y=="F"): print(x,"Farenheit is equal to", (x-32)*5/9)