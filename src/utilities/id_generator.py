"""Id generator"""
from repositories.item_repository import ITEM_REPOSITORY
import shortuuid

class IdGenerator:
    """Generator for item ids"""
    shortuuid.set_alphabet("1234567890")
    
    # def __init__(self):
    #     self.id_number = max([int(item[0]) for item in ITEM_REPOSITORY.find_all()])

    def get_id(self):
        """Updates id and returns new id"""
        s = shortuuid.uuid()
        s_shortened = s[:6]
        return str(s_shortened)
        #self.id_number += 1
        #return str(self.id_number).zfill(4)

ID_GENERATOR = IdGenerator()
