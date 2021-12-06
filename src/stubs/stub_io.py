class StubIO:
    def __init__(self, inputs=None):
        self.inputs = inputs or []
        self.outputs = []

    def write(self, value):
        self.outputs.append(value)

    def read(self, prompt):
        if len(self.inputs) > 0:
            return self.inputs.pop(0)
        return "0"

    def add_input(self, value):
        self.inputs.append(value)

    def guide(self):
        """Guidelines/Menu"""
        menu = (
            "\nValitse toiminto"
            "\n (1) lisää"
            "\n (2) listaa"
            "\n (3) hae"
            "\n (4) muokkaa"
            "\n (5) poista"
            "\n (0) lopeta\n")
        print(menu)