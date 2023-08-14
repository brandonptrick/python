#Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.
number1 = 20
number2 = 300

def number_checker():
    if number1 * number2 <= 1000:
        return number1 * number2
    else:
        return number1 + number2

print(number_checker()) 
