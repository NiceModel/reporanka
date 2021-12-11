"""Library for running robot framework tests."""

from app.app import App
from repositories.item_repository import TEST_ITEM_REPO
from stubs.stub_io import StubIO
from stubs.stub_item_service import StubItemService
from utilities.csv_utilities import clear_csv

class AppLibrary:
    """Services for App"""
    def __init__(self):
        self._io = StubIO()
        self._item_repository = TEST_ITEM_REPO
        self.clear_test_file()
        self._item_service = StubItemService(TEST_ITEM_REPO)
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

    def run_application(self):
        """Run application"""
        self._app.run()

    def clear_test_file(self):
        self._item_repository.delete_all_items()
