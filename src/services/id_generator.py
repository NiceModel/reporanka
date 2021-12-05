from config import DB_PATH
from utilities.csv_utilities import get_last_id

class IdGenerator:
    def __init__(self):
        self._next = get_last_id(DB_PATH)

    def new_id(self):
        self._next += 1
        return self._next

id_generator = IdGenerator()
