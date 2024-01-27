import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

class AESCipher:
    def __init__(self, key_file='./db/aes.key'):
        self.key_file = key_file
        if not os.path.exists(self.key_file):
            self.key = os.urandom(32)  # AES key should be either 16, 24, or 32 bytes
            self.save_key()
        else:
            self.load_key()

    def save_key(self):
        with open(self.key_file, 'wb') as key_file:
            key_file.write(self.key)

    def load_key(self):
        with open(self.key_file, 'rb') as key_file:
            self.key = key_file.read()

    def encrypt(self, message):
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(message.encode()) + padder.finalize()

        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        encrypted_message = encryptor.update(padded_data) + encryptor.finalize()

        return base64.b64encode(iv + encrypted_message).decode('utf-8')
    

    def decrypt(self, encrypted_message):
        iv = encrypted_message[:16]
        encrypted_message = encrypted_message[16:]

        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        padded_message = decryptor.update(encrypted_message) + decryptor.finalize()

        unpadder = padding.PKCS7(128).unpadder()
        decrypted_message = unpadder.update(padded_message) + unpadder.finalize()

        return decrypted_message.decode()

