from Cli.actions.models.password import Password
from Cli.actions.utils.encrypt import AESCipher
from Cli.actions.utils.dbManager import DBManager

class Actions():
    CREATE = 'create'
    READ = 'read'
    UPDATE = 'update'
    LIST = 'list'
    DELETE = 'delete'
    MASS = 'mass'

    def __str__(self):
        return self.value.lower()
    
class Action():
    def __init__(self) -> None:
        self._db_manager = DBManager()
        self._cipher = AESCipher()
    
    def create(self, name, description, key):
        encrypted_key = self._cipher.encrypt(key)
        password = Password(name, description, encrypted_key)
        self._db_manager.save_password(password)
        print(f"Your password is encrypted to: {encrypted_key}")

    def read(self, name):
        password = Password.from_json(self._db_manager.load_password(name))
        print("=============================")
        print(f"Name: \t{password.name}")
        print(f"Description: \t{password.description}")
        print(f"Encrypted_password: \t{password.encrypted_password}")
        print("=============================")
    
    def update(self, name, new_key):
        if self._db_manager.file_exists(name):
            old_password = Password.from_json(self._db_manager.load_password(name))
            new_key_enc = self._cipher.encrypt(new_key)
            new_password = Password(old_password.name, old_password.description, new_key_enc)
            self._db_manager.save_password(new_password)
            print(f"password for key: {old_password.name} updated successfully!!")
            print(f"your new key encrypted value is: {new_key_enc}")
        else:
            print("this file isnt available yet, cant update it")
    
    def delete(self, name):
        if self._db_manager.delete_password(name):
            print("password deleted successfully")
        else:
            print("something went wrong....")

    def list(self):
        passwords_list = self._db_manager.list_passwords()
        for i, password in enumerate(passwords_list):
            password_data = Password.from_json(password)
            print("=============================")
            print(f"{i+1})")
            print(f"Name: \t{password_data.name}")
            print(f"Description: \t{password_data.description}")
            print(f"Encrypted_password: \t{password_data.encrypted_password}")
            print("=============================")

    def mass(self, key):
        for _ in range(10000):
            self._db_manager.append_to_file('mass.txt', self._cipher.encrypt_with_random_length(key))