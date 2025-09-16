'''docstring'''
def cool_div(num1, num2):
    '''docstring'''
    if not num1 % num2:
        return num1 // num2
    return num1 / num2

def calculator(num1, num2):
    '''docstring'''
    print("Thank you!")
    print(f"{num1} + {num2} = {num1 + num2}")
    print(f"{num1} - {num2} = {num1 - num2}")
    if num2:
        print(f"{num1} / {num2} = {cool_div(num1, num2)}")
    else:
        print("Division by zero is not allowed.")
    print(f"{num1} * {num2} = {num1 * num2}")

def main():
    '''docstring'''
    num1 = int(input("Give me the first number: "))
    num2 = int(input("Give me the second number: "))
    calculator(num1, num2)

main()
