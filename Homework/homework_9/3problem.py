# Create a dictionary for the months and amount of days
d = {
    'january': 31,
    'february': 28,
    'march': 31,
    'april':30,
    'may':31,
    'june':30,
    'july':31,
    'august':31,
    'september':30,
    'october':31,
    'november':30,
    "december":31
}

#Create an empty list to order months in
sortedmonths=[]

# Ask user for a month name
name=input("Enter a month name: ")

# create a loop for the amount of days in said month
for i in d:
    if i==name:
        print("There are ",d[i],"days")
sortedmonths+=list(d)
sortedmonths.sort()
print(sortedmonths)
for i in d:
    if d[i]==31:
        print(i,"has 31 days")
    

for num_days in [28, 30, 31]:

    for month in d.keys():
        if d[month] == num_days:
            print("Month: ", month, "Days: ", num_days)