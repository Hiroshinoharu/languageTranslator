from PyQt6.QtWidgets import QVBoxLayout, QWidget, QScrollArea, QLabel, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon

# Define a class named HistoryWindow that inherits from QWidget
class HistoryWindow(QWidget):
    """
    A window that displays a list of histories.

    Args:
        hsitory (dict): A dictionary containing the history items.

    Attributes:
        history (dict): A dictionary containing the history items.

    """
    # Define the constructor method that takes a 'history' parameter
    def __init__(self, history):
        super().__init__() # Call the constructor of the base class (QWidget)
        self.setWindowTitle("History") # Set the window title
        self.setFixedSize(400, 400) # Set the window size
        self.setWindowIcon(QIcon("images/icon.png")) # Set the window icon

        
        # Create a layout for the window
        layout = QVBoxLayout()
        
        # Create a scroll area widget
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True) # Allow the scroll area to be resized
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn) # Show vertical scroll bar
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff) # Hide horizontal scroll bar
        
        # Create a widget to hold the content of the scroll area
        scroll_content = QWidget()
        
        # Create a layout for the scroll content
        scroll_layout = QVBoxLayout()
        
        # Check if the 'history' parameter is a dictionary
        if isinstance(history, dict):
            # Iterate over the key-value pairs in the history dictionary
            for key, value in history.items():
                # Create a label with formatted text
                label = QLabel(f"<h3>{key}</h3><p>{value}</p>")
                label.setWordWrap(True)
                label.setStyleSheet("QLabel { font-weight: bold; font-size: 14px; }")  # Add bold font style and increase font size
                scroll_layout.addWidget(label)
        else:
            error_label = QLabel("<h3>Error: Favorites is not a dictionary.</h3>")
            error_label.setStyleSheet("QLabel { color: red; font-size: 14px; }")  # Add red color and increase font size
            scroll_layout.addWidget(error_label)
            
        # Set the layout for the scroll content widget
        scroll_content.setLayout(scroll_layout)
        
        # Set the scroll content widget as the widget for the scroll area
        scroll_area.setWidget(scroll_content)
        
        # Add the scroll area to the main layout
        layout.addWidget(scroll_area)
        
        # Create a close button
        close_button = QPushButton("Close")
        close_button.clicked.connect(self.close) # Connect the button's clicked signal to the close method of the window
        layout.addWidget(close_button, alignment=Qt.AlignmentFlag.AlignCenter) # Add the button to the layout
        
        # Set the main layout for the window
        self.setLayout(layout)