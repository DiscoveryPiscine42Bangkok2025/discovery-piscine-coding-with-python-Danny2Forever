'''docstring'''
def check_password(password_input):
    '''docstring'''
    password = "Python is awesome"
    if password_input == password:
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")

def main():
    '''docstring'''
    password = input()
    check_password(password)

main()
