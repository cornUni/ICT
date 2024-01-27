from Cli.actions.models.password import Password
from Cli.actions.utils.dbManager import DBManager
def list():
    db_manager = DBManager()
    passwords_list = db_manager.list_passwords()
    for i, password in enumerate(passwords_list):
        password_data = Password.from_json(password)
        print("=============================")
        print(f"{i+1})")
        print(f"Name: \t{password_data.name}")
        print(f"Description: \t{password_data.description}")
        print(f"Encrypted_password: \t{password_data.encrypted_password}")
        print("=============================")