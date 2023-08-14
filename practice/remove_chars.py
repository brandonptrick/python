#Write a program to remove characters from a string starting from zero up to n and return a new string.

def user_input():
    while True:
        word = input("Please type a word: ")
        if word.isalpha():
            break
        else: 
            print("Please enter a valid word.")

    while True:
        n = input("Please enter the number of charecters to remove: ")
        if n.isdigit():
            n = int(n)
            if 0 < n < len(word): 
                break
            else:
                print("Pleaser enter a valid number")
        else:
            print("Please enter a valid number.")
    
    return word, n


user_input()