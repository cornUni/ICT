class CliColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Protocols:
    TCP = 'TCP'
    UDP = 'UDP'

def print_color_string(message, *colors, end='\n'):
    color_sequence = ''.join(color for color in colors)
    print(f"{color_sequence}{message}{CliColors.ENDC}", end=end)


def save_report_file(data, file_address):
    with open(f'output/{file_address}.txt', 'w') as file:
        file.write(data)