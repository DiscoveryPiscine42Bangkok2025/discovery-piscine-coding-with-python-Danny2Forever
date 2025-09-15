'''docstring'''
def isneg(num):
    '''docstring'''
    if num < 0:
        print("This number is negative.")
    elif num > 0:
        print("This number is positive.")
    else:
        print("This number is both positive and negative.")

def mult(num1, num2):
    '''docstring'''
    result = num1 * num2
    print(f"{num1} x {num2} = {result}")
    isneg(result)

def main():
    '''docstring'''
    num1 = int(input("Enter the first number:\n"))
    num2 = int(input("Enter the second number:\n"))
    mult(num1, num2)

main()
