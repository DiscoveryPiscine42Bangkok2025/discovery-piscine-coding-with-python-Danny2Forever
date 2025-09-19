'''docstring'''
import sys
def main():
    '''docstring'''
    if len(sys.argv) == 2:
        print('z'*((sys.argv)[1].count('z')))
    else:
        print("none")

main()
