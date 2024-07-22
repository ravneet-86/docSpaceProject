from remedy_searcher import RemedySearcher
from db_controller import DbController

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

REMEDY_DB_NAME = "avRemedyDb"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print("Creating DB Controller")
    # Create instance of DB controller
    db_controller = DbController(REMEDY_DB_NAME)

    print("DB Controller created")
    # Create remedy searcher which should update the remedies to DB.
    remedy_searcher = RemedySearcher(db_controller)
    print("Remedy Searcher done")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
