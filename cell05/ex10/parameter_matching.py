'''docstring'''
import sys
def main():
    '''docstring'''
    if len(sys.argv)==2:
        para = input("What was the parameter? ")
        if para == sys.argv[1]:
            print("Good job!")
        else:
            print("Nope, sorry...")
    else:
        print("none")

main()
