from Crypto.Cipher import DES as DES_ALGORITHM
from Crypto.Random import get_random_bytes
from algorithms.EncryptionAlgorithm import EncryptionAlgorithm

class DES(EncryptionAlgorithm):
    
    def generate_key(self):
        return get_random_bytes(DES_ALGORITHM.block_size)

    
    def encrypt(self, data, key):
        cipher = DES_ALGORITHM.new(key, DES_ALGORITHM.MODE_ECB)
        ciphertext = cipher.encrypt(self.pad(data.encode('utf8')))
        return ciphertext

    
    def decrypt(self, encrypted_data, key):
        cipher = DES_ALGORITHM.new(key, DES_ALGORITHM.MODE_ECB)
        decrypted_data = cipher.decrypt(encrypted_data)
        return self.unpad(decrypted_data).decode()

    
    def pad(self, data):
        block_size = DES_ALGORITHM.block_size
        padding_length = block_size - (len(data) % block_size)
        padding = bytes([padding_length]) * padding_length
        return data + padding

    
    def unpad(self, data):
        padding_length = data[-1]
        return data[:-padding_length]