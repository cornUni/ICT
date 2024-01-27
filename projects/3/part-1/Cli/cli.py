from Cli.actions.utils.argParser import ArgParser
from Cli.actions.Actions import Action
from Cli.actions import create, delete, list, read, update


class CLI():
    def __init__(self):
        self._argParser = ArgParser()
        self._args = self._argParser.get_args()
        self._parser = self._argParser.parser
        
    
    def execute(self):
        
        if self._args.command == str(Action.CREATE):
            create.create(self._args.passwordName, " ".join(self._args.description), self._args.key)
        
        elif self._args.command == str(Action.LIST):
            list.list()
        
        elif self._args.command == str(Action.READ):
            read.read(" ".join(self._args.passwordName))
        
        elif self._args.command == str(Action.UPDATE):
            update.update(" ".join(self._args.passwordName))
        
        elif self._args.command == str(Action.DELETE):
            delete.delete(" ".join(self._args.passwordName))
        
        else:
            self._parser.print_help()
