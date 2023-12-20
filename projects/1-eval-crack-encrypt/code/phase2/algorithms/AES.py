
from Crypto.Cipher import AES as AES_ALGORITHM
from Crypto.Random import get_random_bytes
from algorithms.EncryptionAlgorithm import EncryptionAlgorithm

class AES(EncryptionAlgorithm):

    def __init__(self):
        self.nonce = 0
        self.iv = 0
    
    
    def generate_key(self):
        return get_random_bytes(AES_ALGORITHM.block_size)

     
    def encrypt(self, data, key):
        cipher = AES_ALGORITHM.new(key, AES_ALGORITHM.MODE_CFB)
        ciphertext = cipher.encrypt(data.encode('utf8'))
        self.iv = cipher.iv
        return ciphertext

     
    def decrypt(self, encrypted_data, key):
        cipher_dec = AES_ALGORITHM.new(key, AES_ALGORITHM.MODE_CFB, self.iv)
        plaintext = cipher_dec.decrypt(encrypted_data)
        return plaintext.decode()

     
    def pad(self, data):
        pass

     
    def unpad(self, data):
        pass