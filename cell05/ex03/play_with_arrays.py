'''docstring'''
def main():
    '''docstring'''
    array = [2, 8, 9, 48, 8, 22, -12, 2]
    new_array = [i+2 for i in array if i > 5]
    result_array = set(new_array)
    print(array)
    print(result_array)

main()
