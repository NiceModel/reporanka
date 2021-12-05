"""Services for App"""

from app.app import App
from stubs.stub_io import StubIO
from services.book_service import BookService
from stubs.stub_book_repository import StubBookRepository

class AppLibrary:
    """Services for App"""
    def __init__(self):
        self._io = StubIO()
        self._book_repository = StubBookRepository()
        self._book_service = BookService(self._book_repository)
        self._app = App(
            self._book_service,
            self._io,
        )

    def input(self, value):
        """Add input to UI"""
        self._io.add_input(value)

    def output_should_contain(self, value):
        """Validation for output"""
        outputs = set(self._io.outputs)

        if value not in outputs:
            raise AssertionError(
                f"Output \"{value}\" is not in {str(outputs)}"
            )

    def run_application(self):
        """Run application"""
        self._app.run()

