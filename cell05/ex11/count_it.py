'''docstring'''
import sys
def main():
    '''docstring'''
    args = sys.argv[1:]
    if len(args):
        print("parameters:", len(args))
        for i in args:
            print(f"{i}: {len(i)}")
    else:
        print("none")

main()
