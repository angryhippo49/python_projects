
# Ask user for text
Text = input("Enter some text: ")

# Count how many articles
ancount = Text.count("an ")
acount = Text.count(" a ")
thecount = Text.count(" the ")

# Print counts

print("There are ",ancount,"ans, ",acount,"as, and ",thecount,"thes.")