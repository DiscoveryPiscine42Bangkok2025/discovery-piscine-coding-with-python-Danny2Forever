'''docstring'''
import sys
def main():
    '''docstring'''
    try:
        print(sys.argv[1].upper())
    except IndexError:
        print("none")

main()
