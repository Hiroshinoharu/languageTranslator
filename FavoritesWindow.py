from PyQt6.QtWidgets import QVBoxLayout, QWidget, QScrollArea, QLabel, QPushButton
from PyQt6.QtCore import Qt

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
        self.setWindowTitle("Favorites")
        self.setFixedSize(400, 400)
        
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
                label = QLabel(f"<b>{key}:</b> {value}")
                label.setWordWrap(True)
                label.setStyleSheet("QLabel { font-weight: bold; }")  # Add bold font style
                scroll_layout.addWidget(label)
        else:
            error_label = QLabel("Error: Favorites is not a dictionary.")
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