"""IO for console"""
class ConsoleIO:
    """IO for console"""
    def write(self, value):
        """Write to console"""
        print(value)

    def read(self, prompt):
        """Read from console"""
        return input(prompt)
