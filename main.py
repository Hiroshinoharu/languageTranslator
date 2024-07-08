# Import the necessary modules
import sys
from PyQt6.QtWidgets import QApplication
from init_ui import TranslatorApp

# Create an application instance
if __name__ == "__main__":
    # Initialize the PyQt6 application
    app = QApplication(sys.argv)
    # Create an instance of the TranslatorApp class
    window = TranslatorApp()
    # Start the application event loop
    sys.exit(app.exec())