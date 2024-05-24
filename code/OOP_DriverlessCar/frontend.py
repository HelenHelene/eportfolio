class Frontend:
    """Class for handling frontend interface for user interaction."""

    def __init__(self, backend):
        """
        Inital frontend with a reference to backend,
        while the backend instance for logging and retrieving history.
        """
        self.backend = backend  

    def menu(self):
        """Display the menu options for user interaction."""
        print("1. Start Engine")
        print("2. Move Car")
        print("3. Stop Car")
        print("4. View History")
        print("5. Exit")

    def get_data(self):
        """Retrieve and display the action history from backend."""
        history = self.backend.get_history()
        for record in history:
            print(record)