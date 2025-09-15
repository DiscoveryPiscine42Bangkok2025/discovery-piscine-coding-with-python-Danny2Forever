'''docstring'''
def isneg(num):
    '''docstring'''
    if num < 0:
        print("This number is negative.")
    elif num > 0:
        print("This number is positive.")
    else:
        print("This number is both positive and negative.")

def main():
    '''docstring'''
    num = input()
    isneg(int(num))

main()
