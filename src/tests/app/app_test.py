import unittest
from app.app import App

class StubIO:
    def __init__(self):
        self.inputs = []

    def write(self, value):
        pass

    def read(self, prompt):
        return "0"

class StubItemService:
    def __init__(self):
        pass


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = App(StubItemService(), StubIO())

    def test_init(self):
        self.assertFalse(self.app.running)

    def test_main_loop(self):
        with self.assertRaises(SystemExit) as cm:
            self.app.run()

        self.assertEqual(cm.exception.code, 0)