'''docstring'''
def isfloat(num):
    '''docstring'''
    if num.is_integer():
        print("This number is an integer.")
    else:
        print("This number is a decimal.")

def main():
    '''docstring'''
    num = float(input("Give me a number: "))
    isfloat(num)

main()
