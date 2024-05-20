import datetime

class Backend:
    """Class for handling backend operations, collect and store action history."""

    def __init__(self):
        """Initial backend history with empty list."""
        self.history = []

    def update_data(self, data):
        """Update backend history with new record."""
        timestamp = datetime.datetime.now()
        self.history.append((timestamp, data))  # Append a tuple of timestamp and data to history.
        print(f"Backend updated: {data}")

    def get_history(self):
        """Return history of logged data."""
        return self.history