"""Main program"""
from services.book_service import BookService
from console_io import ConsoleIO
from app import App


def main():
    """Runs main program"""
    book_service = BookService()
    console_io = ConsoleIO()
    app = App(book_service, console_io)

    app.run()


if __name__ == "__main__":
    main()
