"""Id generator"""
from repositories.item_repository import ITEM_REPOSITORY

class IdGenerator:
    """Generator for item ids"""
    
    def __init__(self):
        self.id_number = max([int(item[0]) for item in ITEM_REPOSITORY.find_all()])

    def get_id(self):
        """Updates id and returns new id"""
        
        self.id_number += 1
        return self.id_number 

ID_GENERATOR = IdGenerator()