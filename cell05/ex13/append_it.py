'''docstring'''
import sys
def main():
    '''docstring'''
    if not len(sys.argv) == 1:
        for i in sys.argv[1:]:
            if not i.endswith("ism"):
                print(i+"ism")
    else:
        print("none")

main()
