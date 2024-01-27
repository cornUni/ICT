from Cli.actions.models.password import Password
from Cli.actions.utils.dbManager import DBManager
def read(name):
    db_manager = DBManager()
    password = Password.from_json(db_manager.load_password(name))
    print("=============================")
    print(f"Name: \t{password.name}")
    print(f"Description: \t{password.description}")
    print(f"Encrypted_password: \t{password.encrypted_password}")
    print("=============================")