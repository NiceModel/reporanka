from app import App
# from console_io import ConsoleIO 
from stub_io import StubIO
from repositories.book_repository import BookRepository
from services.io_service import IOService
from services.book_service import BookService
import sys
from io import StringIO

class AppLibrary:
    def __init__(self):
        # self._io = ConsoleIO()
        self._io = StubIO()
        self._book_repository = BookRepository()
        self._io_service = IOService()
        self._book_service = BookService(self._book_repository)  
        self.running = True
        self.ohjeet = (
            "\nValitse toiminto"
            "\n (1) lisää"
            "\n (2) listaa"
            "\n (3) hae"
            "\n (0) lopeta\n"  
        )
        self._app = App(
            self._book_service,
            self._io,
        )

    def input(self, value):
        self._io.add_input(value)
        print(
                f"Input \"{value}\" is in {str(input)}"
            )

    def output_should_contain(self, value):
        outputs = self._io.outputs

        if not value in outputs:
            raise AssertionError(
                f"Output \"{value}\" is not in {str(outputs)}"
            )

    def run_application(self):
        self._app.run()

    # def create_user(self, username, password):
    #     self._user_service.create_user(username, password)