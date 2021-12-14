"""Library for running robot framework tests."""

from app.app import App
from services.item_service import ItemService
from stubs.stub_io import StubIO
from stubs.stub_item_repository import StubItemRepository
from repositories.item_repository import ItemRepository

class AppLibrary:
    """Services for App"""
    def __init__(self):
        self._io = StubIO()
        self._item_test_repository = StubItemRepository()
        self._item_repository = ItemRepository()
        self.clear_test_file()
        self._item_service = ItemService(self._item_test_repository)
        self._app = App(
            self._item_service,
            self._io,
        )

    def input(self, value):
        """Add input to UI"""
        self._io.add_input(value)

    def output_should_contain(self, value):
        """Validation #1 for output"""
        outputs = set(self._io.outputs)

        if value not in outputs:
            raise AssertionError(
                f"Output \"{value}\" is not in {str(outputs)}"
            )
        outputs.clear()

    def output_should_not_contain(self, value):
        """Validation #2 for output, negation to validation #1"""
        outputs = set(self._io.outputs)

        if value in outputs:
            raise AssertionError(
                f"Output \"{value}\" should NOT be in {str(outputs)}"
            )
        outputs.clear()

    def output_should_cover(self, value1, value2):
        """Validation #3 for output, for 2 attributes"""
        outputs = ""
        outputs = self._io.outputs

        if value1 not in outputs:
            raise AssertionError(
                f"Output \"{value1}\" is not in {str(outputs)}"
            )
        if value2 not in outputs:
            raise AssertionError(
                f"Output \"{value2}\" is not in {str(outputs)}"
            )
        outputs = ""

    def run_application(self):
        """Run application"""
        self._app.run()

    def clear_test_file(self):
        """Clears the test file"""
        self._item_test_repository.delete_all_items()

    def clear_outputs(self):
        """Clear previous outputs"""
        self._io.clear_outputs()
