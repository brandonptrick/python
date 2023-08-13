
def user_input():
    while True:
        num = input("Please enter a number: ")
        if num.isdigit():
            num = int(num)
            if num > 0: 
                break
        else:
            print("Please enter a valid number.")
    return num


def odd_or_even():
    choice = user_input()
    if choice % 2 == 0:
        print("Your number is even.")
    else:
        print("Your number is odd.")
    

while True:
    odd_or_even()
    if input("Press enter to continue, q to quit ") == "q":
        break