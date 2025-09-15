'''docstring'''
def whats_your_name(first_name, last_name):
    '''docstring'''
    whole_name = f"{first_name} {last_name}"
    print(f"Hey, what's your first name? : {first_name}")
    print(f"And your last name? : {last_name}")
    print(f"Well, pleased to meet you, {whole_name}.")

def main():
    '''docstring'''
    first_name = input("")
    last_name = input("")
    whats_your_name(first_name, last_name)

main()
