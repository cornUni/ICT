import argparse
from Cli.actions.Actions import Action
class ArgParser():
    def __init__(self):
        self._parser = argparse.ArgumentParser(description="Password Manager")
        subparsers = self._parser.add_subparsers(dest="command")

        # New Password command
        new_parser = subparsers.add_parser(Action.CREATE, help="Create a new password")
        new_parser.add_argument("-n", "--passwordName", type=str, help="Name of the new password")
        new_parser.add_argument("-c", "--description", type=str, nargs='+', required=True, help="Description of the new password")
        new_parser.add_argument("-key", type=str, help="Encryption key")

        # Show Passwords command
        show_parser = subparsers.add_parser(Action.LIST, help="Show all passwords")

        # Select Password command
        select_parser = subparsers.add_parser(Action.READ, help="Select a password")
        select_parser.add_argument("passwordName", type=str, nargs='+', help="Name of the password to select")

        # Update Password command
        update_parser = subparsers.add_parser(Action.UPDATE, help="Update a password")
        update_parser.add_argument("passwordName", type=str, nargs='+', help="Name of the password to update")

        # Delete Password command
        delete_parser = subparsers.add_parser(Action.DELETE, help="Delete a password")
        delete_parser.add_argument("passwordName", type=str, nargs='+', help="Name of the password to delete")
   
    def get_args(self):
        args =  self._parser.parse_args()
        return args
    
    @property
    def parser(self):
        return self._parser

   