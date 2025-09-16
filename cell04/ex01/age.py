'''docstring'''
def age(age_input):
    '''docstring'''
    print(f"You are currently {age_input} years old.")
    for i in range(10, 31, 10):
        print(f"In {i} years, you'll be {age_input+i} years old.")

def main():
    '''docstring'''
    age_input = int(input("Please tell me your age: "))
    age(age_input)

main()
