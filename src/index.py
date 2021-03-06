"""Main program"""
from services.item_service import ItemService
from app.console_io import ConsoleIO
from app.app import App


def main():
    """Runs the main program"""
    item_service = ItemService()
    console_io = ConsoleIO()
    app = App(item_service, console_io)

    app.run()

if __name__ == "__main__":
    main()
