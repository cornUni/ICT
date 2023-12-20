from abc import ABC, abstractmethod
import os


class EncryptionAlgorithm(ABC):
    @abstractmethod
    def generate_key(self):
        pass

    @abstractmethod
    def encrypt(self, data, key):
        pass

    @abstractmethod
    def decrypt(self, encrypted_data, key):
        pass

    @abstractmethod
    def pad(self, data):
        pass

    @abstractmethod
    def unpad(self, data):
        pass