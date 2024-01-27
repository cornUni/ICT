from enum import Enum

class Action():
    CREATE = 'create'
    READ = 'read'
    UPDATE = 'update'
    LIST = 'list'
    DELETE = 'delete'

    def __str__(self):
        return self.value.lower()
