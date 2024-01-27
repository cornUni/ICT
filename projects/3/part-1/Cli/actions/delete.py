from Cli.actions.utils.dbManager import DBManager
def delete(name):
    db_manager = DBManager()
    if db_manager.delete_password(name):
        print("password deleted successfully")
    else:
        print("something went wrong....")