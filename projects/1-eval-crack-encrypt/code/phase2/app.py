from algorithms.AES import AES
from algorithms.DES import DES
from algorithms.RSA import RSA

def read_from_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
        return data
def save_to_file(filename, data):
    try:
        with open(filename, 'w') as file:
            file.write(str(data))
        return True
    except Exception as e:
        print(f"Error: {str(e)}")
        return False
    


def algorithm_handler(algorithm):
    if algorithm == 'AES':
        return AES()
    elif algorithm == 'DES':
        return DES()
    elif algorithm == 'RSA':
        return RSA()

def cryptography_handler(algorithm, filename):
    cryptography__algorithm = algorithm_handler(algorithm)
    key = cryptography__algorithm.generate_key()
    data = read_from_file(f'data/{filename}')

    encrypted_data = cryptography__algorithm.encrypt(data, key)
    save_to_file(f'output/{algorithm}_enc_{file_name}', encrypted_data)

    decrypted_data = cryptography__algorithm.decrypt(encrypted_data, key)

    save_to_file(f'output/{algorithm}_dec_{file_name}', decrypted_data)
    




if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser(description='Accept a string as a command-line argument')
    parser.add_argument('-a', '--algorithm', type=str, choices=["RSA", "DES", "AES"],help='Password to guess')
    parser.add_argument('-f', '--file', type=str,help='Password to guess')
    args = parser.parse_args()
    algorithm = args.algorithm
    file_name = args.file
    cryptography_handler(algorithm, file_name)
