#Write a program to accept a string from the user and display characters that are present at an even index number.

str = input("Type a string to use: ")
print(f"Original string is {str}.")

size = len(str)
print("Printing only even index chars")
for i in range(0, size - 1, 2):
    print("index[", i, "]", str[i])

