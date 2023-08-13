CURRENT_YEAR = 2023
CAL_AGE = 100

def user_input():
    while True:
        name = input("Please enter your name: ")
        if name.isalpha():
            break
        else:
            print("Please enter a valid name.")
    while True:
        age = input("Please enter your age: ")
        if age.isdigit():
            age = int(age)
            if age <= 0:
                print("Please enter a valid age.")
            else:
                break
        else:
            print("Please enter a valid age.")

    return name, age


def years_to_hundred():
    name, age = user_input()[:]
    difference = CAL_AGE - age
    year_hundred = CURRENT_YEAR + difference
    print(f"{name.title()}, you have {difference} years till you're {CAL_AGE} years old.")
    print(f"The year will be {year_hundred}.")


years_to_hundred()


