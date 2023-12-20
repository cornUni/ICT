import json


class Password_Strength:
    UNACCEPTABLE = 'unacceptable'
    WEAK = "weak"
    MODERATE = "moderate"
    ACCEPTABLE = 'acceptable'
    STRONG = 'strong'

def cache_passwords(data):
    with open('cache_pass.json', 'w') as file:
        json.dump(data, file)

def get_cached_passwords():
    try:
        with open('cache_pass.json', 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return None

def strength_score(password):
    score = 0
    warning_notes = []

    if len(password) >= 8:
        score +=1
    else:
        warning_notes.append("choose a password with length of 8 or more")
    if any(char.isupper() for char in password):
        score += 1
    else:
        warning_notes.append("better use at least an uppercase char in your password")
    if any(char.islower() for char in password):
        score += 1
    else:
        warning_notes.append("better use at least a lowercase char in your password")
    if any(char.isdigit() for char in password):
        score += 1
    else:
        warning_notes.append("better use at least a digit in your password")
    if any(char in r'!@#$%^&*()-_=+[]{}|;:,.<>?/~`' for char in password):
        score += 1
    else:
        warning_notes.append("better use at least a special character in your password")

    return score, warning_notes


def evalute_password_strength(password):
    cache = get_cached_passwords()
    if password in cache:
        print(f'password already checked, The strength level is: {cache[password]}')
        return
    score, warning_notes = strength_score(password)
    strength = ''
    if score == 0:
        strength = Password_Strength.UNACCEPTABLE.capitalize()
    elif score == 1:
        strength = Password_Strength.WEAK.capitalize()
    elif score == 2:
        strength = Password_Strength.MODERATE.capitalize()
    elif score == 3:
        strength = Password_Strength.ACCEPTABLE.capitalize()
    elif score == 4:
        strength = Password_Strength.ACCEPTABLE.capitalize()
    elif score == 5:
        strength = Password_Strength.STRONG.capitalize()
    
    print(f'your password is: {strength}\n')
    if score < 5:
        print('here are few advices to make stronger passwords:', end='\n>')
        print('\n>'.join(warning_notes))

    cache[password] = strength
    cache_passwords(cache)
if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser(description='Accept a string as a command-line argument')
    parser.add_argument('-pass', '--password_arg', type=str, help='A string argument')
    args = parser.parse_args()
    entry_password = args.password_arg
    evalute_password_strength(entry_password)
