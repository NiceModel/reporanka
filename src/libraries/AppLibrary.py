"""Library for running robot framework tests."""

from app.app import App
from stubs.stub_io import StubIO
from stubs.stub_item_repository import StubItemRepository
from services.item_service import ItemService

class AppLibrary:
    """Services for App"""
    def __init__(self):
        self._io = StubIO()
        self._item_repository = StubItemRepository()
        self._item_service = ItemService(self._item_repository)
        self._app = App(
            self._item_service,
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
