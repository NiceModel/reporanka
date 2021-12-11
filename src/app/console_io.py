from tabulate import tabulate

"""IO for console"""
class ConsoleIO:
    """IO for console"""
    def write(self, value, table=False):
        """Write to console"""
        if table:
            print(tabulate(value, headers='firstrow', tablefmt='fancy_grid'))
        else:
            print(value)

    def read(self, prompt):
        """Read from console"""
        return input(prompt)
