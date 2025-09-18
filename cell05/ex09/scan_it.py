'''docstring'''
import sys
def main():
    '''docstring'''
    if len(sys.argv)==3:
        print(sys.argv[2].count(sys.argv[1]))
    else:
        print("none")

main()
