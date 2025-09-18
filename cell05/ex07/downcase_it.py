'''docstring'''
import sys
def main():
    '''docstring'''
    try:
        print(sys.argv[1].lower())
    except IndexError:
        print("none")

main()
