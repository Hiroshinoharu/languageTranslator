from PyQt6.QtWidgets import QApplication
from init_ui import TranslatorApp

# Create an application instancE
if __name__ == "__main__":
    app = QApplication([])
    window = TranslatorApp()
    app.exec()