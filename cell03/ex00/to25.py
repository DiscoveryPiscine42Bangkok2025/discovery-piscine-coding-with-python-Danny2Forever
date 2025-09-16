'''docstring'''
def to25(num):
    '''docstring'''
    if num >= 25:
        print("Error")
    else:
        for i in range(num, 26):
            print("Inside the loop, my variable is", i)

def main():
    '''docstring'''
    num = int(input("Enter a number less than 25\n"))
    to25(num)

main()
