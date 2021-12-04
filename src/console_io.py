"""IO for console"""
class ConsoleIO:
    """IO for console"""
    def write(self, value):
        """Write to console"""
        print(value)

    def read(self, prompt):
        """Read from console"""
        return input(prompt)

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