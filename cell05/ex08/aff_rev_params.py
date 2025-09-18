'''docstring'''
import sys
def main():
    """docstring"""
    if len(sys.argv) < 3:
        print("none")
    else:
        for i in range(len(sys.argv) - 1, 0, -1):
            print(sys.argv[i])

main()
