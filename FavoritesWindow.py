from PyQt6.QtWidgets import QVBoxLayout, QWidget, QScrollArea, QLabel, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon 

class FavoritesWindow(QWidget):
    """
    A window that displays a list of favorites.

    Args:
        favorites (dict): A dictionary containing the favorite items.

    Attributes:
        favorites (dict): A dictionary containing the favorite items.

    """
    # Initialize the class
    def __init__(self, favorites):
        super().__init__()
        self.setWindowTitle("Favorites") # Set the window title
        self.setFixedSize(400, 400) # Set the window size
        self.setWindowIcon(QIcon("images/icon.png")) # Set the window icon
        
        # Create a layout
        layout = QVBoxLayout()
        
        # Create a scroll area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        # Scroll content
        scroll_content = QWidget()
        
        # Scroll layout
        scroll_layout = QVBoxLayout()
        
        if isinstance(favorites, dict):
            for key, value in favorites.items():
                # Create a label with formatted text
                label = QLabel(f"<h3>{key}</h3><p>{value}</p>")
                label.setWordWrap(True)
                label.setStyleSheet("QLabel { font-weight: bold; font-size: 14px; }")  # Add bold font style and increase font size
                scroll_layout.addWidget(label)
        else:
            error_label = QLabel("<h3>Error: Favorites is not a dictionary.</h3>")
            error_label.setStyleSheet("QLabel { color: red; font-size: 14px; }")  # Add red color and increase font size
            scroll_layout.addWidget(error_label)
            
        scroll_content.setLayout(scroll_layout)
        scroll_area.setWidget(scroll_content)
        scroll_area.setWidgetResizable(True)
        
        layout.addWidget(scroll_area)
        
        # Close button
        close_button = QPushButton("Close")
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)
