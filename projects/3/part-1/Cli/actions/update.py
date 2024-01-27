from Cli.actions.utils.dbManager import DBManager
from Cli.actions.models.password import Password
from Cli.actions.utils.encrypt import AESCipher
def update(name):
    db_manager = DBManager()
    cipher = AESCipher()
    if db_manager.file_exists(name):
        new_key = input("please enter new value for key\n>")
        old_password = Password.from_json(db_manager.load_password(name))
        new_key_enc = cipher.encrypt(new_key)
        new_password = Password(old_password.name, old_password.description, new_key_enc)
        db_manager.save_password(new_password)
        print(f"password for key: {old_password.name} updated successfully!!")
        print(f"your new key encrypted value is: {new_key_enc}")
    else:
        print("this file isnt available yet, cant update it")