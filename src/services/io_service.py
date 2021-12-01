"""Service for reading from and writing to the items datafile"""

class IOService():
    """Service for reading from and writing to the items datafile"""
    def read(self):
        """Reads from the datafile.

        Returns:
            A tuple of (item type: string, item fields: list)
        """

        with open("src/data/items.csv", "r") as file:
            next(file)
            return [(item[0], item[1].split(",")) for item in file]

    def write(self, item_type, item_fields):
        """Writes to the datafile.

        Writes in two columns:
            item type: string, item fields: list
        """

        with open("src/data/items.csv", "a") as file:
            file.write(f"\n{item_type},{item_fields}")
