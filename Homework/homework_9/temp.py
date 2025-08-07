# Create a dictionary for usernames and passwords

logins={
    "Sathvik":")odHoj9065",
    "Sethuraman":"1000infinity",
    "Delta":"8 threads",
    "compression":"lines",
    "Sethurmamany":"100",
    "main":"004f3",
    "forty":"40",
    "sathvikrox":"rocksrock",
    "sathubathu":"coolguy46",
    "sathbickee":"secretsathvik"
    }
condition=True

# allow the user to keep entering usernames and passwords with an infinite loop
while condition==True:
    username=input("What is the username for the login? ")
    if username not in logins:
        print("That is not a valid username. Please try again")
    else:
        password=input("What is the password? ")
        if logins[username] == password:
            print("Correct")
        else:
            print("incorrect please try again")