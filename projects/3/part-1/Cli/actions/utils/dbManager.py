import glob
import os

class DBManager:
    def __init__(self):
        self.base_path = './db/keys/'

    def save_password(self, password_obj):
        filename = f"{self.base_path}{password_obj.name}.txt"
        with open(filename, 'w') as file:
            file.write(password_obj.to_json())

    def load_password(self, name):
        filename = f"{self.base_path}{name}.txt"
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                return file.read()
        return None
    
    def delete_password(self, name):
        filename = f"{self.base_path}{name}.txt"
        if os.path.exists(filename):
            os.remove(filename)
            return True
        return False
    
    def file_exists(self, name):
        filename = f"{self.base_path}{name}.txt"
        return os.path.exists(filename)
    
    def list_passwords(self):
        password_files = glob.glob(f"{self.base_path}*.txt")          
        passwords = []
        for file in password_files:
            with open(file, 'r') as f:
                password_data = f.read()
                passwords.append(password_data)
        return passwords