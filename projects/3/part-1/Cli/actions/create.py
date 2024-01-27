from Cli.actions.models.password import Password
from Cli.actions.utils.encrypt import AESCipher
from Cli.actions.utils.dbManager import DBManager


def create(name, description, key):
    print(f'create {name} with d of {description} and k of {key}')
    cipher = AESCipher()
    db_manager = DBManager()
    encrypted_key = cipher.encrypt(key)
    password = Password(name, description, encrypted_key)
    db_manager.save_password(password)
    print(f"Your password is encrypted to: {encrypted_key}")