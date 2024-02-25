import json
import base64
class Password:
    def __init__(self, name, description, encrypted_password):
        self.name = name
        self.encrypted_password = encrypted_password
        self.description = description

    def to_json(self):
        return json.dumps({
            "name": self.name,
            "description": self.description,
            "encrypted_password": self.encrypted_password
        })

    @staticmethod
    def from_json(json_str):
        data = json.loads(json_str)
        return Password(data['name'], data['description'], data['encrypted_password'])