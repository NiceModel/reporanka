"""Module for reading/writing from/to the console."""
from tabulate import tabulate

class ConsoleIO:
    """IO for console"""
    def write(self, value, table=False):
        """Write to console.

        args:
            value: str: text to be written
            table: bool: False by default, true if wanted output is a table
        """
        if table:
            print(tabulate(value, headers='firstrow', tablefmt='fancy_grid'))
            
        else:
            print(value)

    def read(self, prompt):
        """Read from console.

        args:
            prompt: str: writes prompt for input in console
        """
        return input(prompt)
