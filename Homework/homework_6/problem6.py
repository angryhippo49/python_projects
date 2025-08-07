s = input("Enter a string: ")
num = 0

for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        num += 1

print("Number of times a character is repeated twice consecutively:", num)