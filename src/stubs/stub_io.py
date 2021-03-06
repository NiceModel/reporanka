"""Stub module for running Robot framework tests."""
class StubIO:
    """Stub for Console IO."""
    def __init__(self, inputs=None):
        self.inputs = inputs or []
        self.outputs = []

    def write(self, value, table=False):
        """Write to console."""
        if table:
            for val in value:
                if isinstance(val, str):
                    self.outputs.append(val)
                else:
                    for itm in val:
                        self.outputs.append(itm)
        else:
            self.outputs.append(value)

    def read(self, prompt):
        """Read from console."""
        if len(self.inputs) > 0:
            return self.inputs.pop(0)
        return "0"

    def add_input(self, value):
        """Add inputs to predefined values for test purposes."""
        self.inputs.append(value)

    def clear_outputs(self):
        """Clear previous outputs"""
        self.outputs = []