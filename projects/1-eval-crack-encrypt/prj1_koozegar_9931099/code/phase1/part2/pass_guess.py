import itertools
import string
import time



def bruteforce_generator(length, search_space):
    iterable = []

    if search_space == 'NO':
        iterable = string.digits
    elif search_space == 'NL':
        iterable = string.digits + string.ascii_lowercase
    elif search_space == 'LO':
        iterable = string.ascii_lowercase
    elif search_space == 'NLU':
        iterable = string.digits + string.ascii_uppercase +string.ascii_lowercase


    return [''.join(p) for p in itertools.product(iterable, repeat=length)]

def find_match(password, password_list):
    attempt_count = 0

    for p in password_list:
        attempt_count += 1
        if p == password:
            return attempt_count
    return None



def guess_password(password_value, mode_value, search_space_value, additional_args_value):
    password_len = len(password_value)
    passwords =[]

    start_time = time.time()

    if mode_value == 1:
        passwords = bruteforce_generator(password_len, search_space_value)
    elif mode_value == 2:
        first_char = password_value[0]
        passwords = bruteforce_generator(password_len - 1, search_space_value)
        passwords = [first_char+p for p in passwords]
    elif mode_value == 3:
        first_k_chars = password_value[:additional_args_value]
        new_len = password_len - additional_args_value
        passwords = bruteforce_generator(new_len, search_space_value)
        passwords = [first_k_chars + p for p in passwords]
    else:
        print("Unknown mode")

    result = find_match(password_value, passwords)

    if result:
        end_time = time.time()
        interval = end_time - start_time
        return result, interval
    else:
        return None

    

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser(description='Accept a string as a command-line argument')

    parser.add_argument('-p', '--password', type=str, help='Password to guess')
    parser.add_argument('-m', '--mode', type=int, choices=[1, 2, 3], help='Mode: 1 - Standard, 2 - Search (first char), 3 - Search (first k chars)')
    parser.add_argument('-s', '--search-space', type=str, choices=['NO', 'NL', 'LO', 'NLU'], help='Search Space: 1 - Numbers, 2 - Numbers and Lowercase Letters, 3 - Lowercase Letters, 4 - Numbers, Lowercase Letters, and Uppercase Letters')
    parser.add_argument('-k', '--additional-args', type=int, help='Additional arguments (used in search mode when specifying the first k chars)')
    
    args = parser.parse_args()
    
    password_value = args.password
    mode_value = args.mode
    search_space_value = args.search_space
    additional_args_value = args.additional_args

    if password_value and mode_value and search_space_value:
        result = guess_password(password_value, mode_value, search_space_value, additional_args_value)
        if result:
            attempts, interval = result
            print(f'It took {attempts} attempts and {interval} seconds to crack the desired password')
        else:
            print('Couldnt find password')
    else:
        print('Please provide all required arguments.')

