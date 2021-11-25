from repositories.book_repository import BookRepository
from services.book_service import BookService
from console_io import ConsoleIO
from app import App


def main():
    book_repository = BookRepository()
    book_service = BookService(book_repository)
    console_io = ConsoleIO()
    app = App(book_service, console_io)

    app.run()

if __name__ == "__main__":
    main()