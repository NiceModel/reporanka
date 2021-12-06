"""Main program"""
from services.item_service import ItemService
from app.console_io import ConsoleIO
from app.app import App


def main():
    """Runs main program"""
    item_service = ItemService()
    console_io = ConsoleIO()
    app = App(item_service, console_io)

    app.run()
1

if __name__ == "__main__":
    main()
