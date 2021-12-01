"""Services for App"""

from app import App
from stub_io import StubIO
from stub_io_service import StubIOService
from services.book_service import BookService
from stub_book_repository import StubBookRepository


class AppLibrary:
    """Services for App"""
    def __init__(self):
        self._io = StubIO()
        self._io_service = StubIOService()
        self._book_repository = StubBookRepository(self._io_service)
        self._book_service = BookService(self._book_repository)
        self._app = App(
            self._book_service,
            self._io,
        )

    def input(self, value):
        """Add input to UI"""
        self._io.add_input(value)
        # print(
        #         f"Input \"{value}\" is in {str(input)}"
        #     )

    def output_should_contain(self, value):
        """Validation for output"""
        outputs = set(self._io.outputs)

        if value not in outputs:
            raise AssertionError(
                f"Output \"{value}\" is not in {str(outputs)}"
            )

    def read(self):
        """Read from input"""
        self._io_service.read()

    def write(self, value, book):
        """Write from input"""
        writetext = set(self._io_service.write(book))

        if value not in writetext:
            raise AssertionError(
                f"Output \"{value}\" is not in {str(writetext)}"
            )

    def run_application(self):
        """Run application"""
        self._app.run()

    # def create_user(self, username, password):
    #     self._user_service.create_user(username, password)
