'''docstring'''
def i_got_that(text):
    '''docstring'''
    while text != "STOP":
        text = input("I got that! Anything else? : ")

def main():
    '''docstring'''
    text = input("What you gotta say? : ")
    i_got_that(text)

main()
