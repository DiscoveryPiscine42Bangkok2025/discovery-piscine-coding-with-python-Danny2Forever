'''docstring'''
def multiplication_table(num):
    '''docstring'''
    for i in range(0, 10):
        print(f"{i} x {num} = {num*i}")

def main():
    '''docstring'''
    num = int(input("Enter a number\n"))
    multiplication_table(num)

main()
