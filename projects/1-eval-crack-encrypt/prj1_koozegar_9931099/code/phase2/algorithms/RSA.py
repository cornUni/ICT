from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from algorithms.EncryptionAlgorithm import EncryptionAlgorithm

class RSA(EncryptionAlgorithm):
    def generate_key(self):
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend
        )
        public_key = private_key.public_key

        return private_key, public_key
    
    def encrypt(self, data, key):
        _ , public_key = key
        print('pub: ',public_key())
        cipher = public_key().encrypt(
            data.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        return cipher
    

    def decrypt(self, data, key):
        private, _ = key
        plaintext = private.decrypt(
            data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return plaintext.decode()


    def pad(self, data):
        return data
    def unpad(self, data):
        return data