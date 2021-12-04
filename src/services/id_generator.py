class IdGenerator:
    def __init__(self):
        self._next = 0

    def new_id(self):
        self._next = self._next + 1
        return self._next


id_generator = IdGenerator()
