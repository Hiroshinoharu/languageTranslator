from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QComboBox, QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt
from googletrans import Translator, LANGUAGES # Import the required libraries

class TranslatorApp(QMainWindow):
    
    # Constructor
    def __init__(self):
        super().__init__()
        self.translator = Translator() # Create a translator object
        self.initUI() # Initialize the UI
     
    # Initialize the UI   
    def initUI(self):
        # Configure the main layout
        layout = QVBoxLayout() # Create a vertical layout
        
        #Variables set for icon buttons
        settings_icon = QPushButton("⚙️")
        favorites_icon = QPushButton("⭐")
        heart_icon = QPushButton("❤️")
        history_icon = QPushButton("🕒")
        speaker_icon = QPushButton("🔊")
        copy_icon = QPushButton("📋")
        
        # Header section
        header_icons = QHBoxLayout() # Create a horizontal layout
        spacer  = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum) # Create a spacer
        header_icons.addItem(spacer) # Add the spacer to the header
        
        # Adding icons to the top right of the GUI
        header_icons.addWidget(settings_icon) # Add the settings icon
        header_icons.addWidget(history_icon) # Add the history icon
        header_icons.addWidget(favorites_icon) # Add the favorites icon
        
        # Logo image
        image_label = QLabel()
        pixmap = QPixmap("images/logo.png")
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                
        #Language selection section
        language_selction_layout = QHBoxLayout() # Create a horizontal layout
        
        # Source language selection section
        source_language_combobox = QComboBox() # Create a combo box for the source language
        source_language_combobox.addItems(LANGUAGES.values()) # Add the languages to the combo box
        source_language_combobox.setCurrentText("english") # Set the default language to English
                       
        # Swap language button
        swap_language_button = QPushButton("🔄")
        swap_language_button.clicked.connect(lambda: self.switch_languages(source_language_combobox,dest_language_combobox)) # When the swap button is clicked, call the switch_languages method
        
        # Target language selection section
        dest_language_combobox = QComboBox() # Create a combo box for the source language
        dest_language_combobox.addItems(LANGUAGES.values()) # Add the languages to the combo box
        dest_language_combobox.setCurrentText("spanish") # Set the default language to Spanish
        
        # Add the source language, swap button and target language to the layout
        language_selction_layout.addWidget(source_language_combobox) # Add the source language combo box
        language_selction_layout.addWidget(swap_language_button) # Add the swap button
        language_selction_layout.addWidget(dest_language_combobox) # Add the target language combo box
        language_selction_layout.setSpacing(10) # Set the spacing between the language selection sections
        language_selction_layout.setContentsMargins(10, 10, 10, 10) # Set the margins for the language selection sections
        
        # Text input section
        text_area_layout = QHBoxLayout() # Create a horizontal layout
        
        # Input text area
        input_text = QPlainTextEdit() # Create a plain text edit for the input text
        input_text.setPlaceholderText("Enter text to translate...") # Add placeholder text
        
        # Output text area
        output_text = QPlainTextEdit() # Create a plain text edit for the output text
        output_text.setReadOnly(True) # Set the output text area to read only
        
        # Add the input and output text areas to the layout
        text_area_layout.addWidget(input_text)
        text_area_layout.addWidget(output_text)
        text_area_layout.setSpacing(10) # Set the spacing between the text areas
        text_area_layout.setContentsMargins(10, 10, 10, 10) # Set the margins for the text areas
                
        # text controls
        textControlsLayout = QHBoxLayout()
        spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        textControlsLayout.addItem(spacer) # Add the spacer to the text controls layout
        
        # Translate button
        translate_button = QPushButton("Translate")
        # When the translate button is clicked, call the translate_text method
        translate_button.clicked.connect(lambda: self.translate_text(source_language_combobox.currentText(), dest_language_combobox.currentText(), input_text.toPlainText(), output_text))        
        
        # Add the output text controls to the layout
        textControlsLayout.addWidget(translate_button, 1, Qt.AlignmentFlag.AlignLeft) 
        textControlsLayout.addWidget(speaker_icon)
        textControlsLayout.addWidget(copy_icon)
        textControlsLayout.addWidget(heart_icon)
        textControlsLayout.setSpacing(10)
        textControlsLayout.setContentsMargins(10, 10, 10, 10)
              
        # Add all the sections to the main layout
        layout.addLayout(header_icons) # Add the header icons to the main layout
        layout.addWidget(image_label) # Add the logo image to the main layout
        layout.addLayout(language_selction_layout) # Add the language selection section to the main layout
        layout.addLayout(text_area_layout) # Add the text area section to the main layout
        layout.addLayout(textControlsLayout) # Add the output text controls to the main layout
        
        # Set the main layout to the main widget
        main = QWidget()
        main.setLayout(layout) # Set the layout of the main widget
        self.setCentralWidget(main) # Set the main widget as the central widget
        self.setWindowTitle("Lingualink Translator") # Set the window title
        self.setWindowIcon(QIcon("images/icon.png")) # Set the window icon
        self.setFixedSize(714, 520) # Set the window size
        self.show() # Show the window
            
    # Method to translate the text
    def translate_text(self, source_lang, dest_lang, text, output_text):
        if not text:
            return output_text.setPlainText("Please enter text to translate")
        result = self.translator.translate(text, src=source_lang, dest=dest_lang)
        return output_text.setPlainText(result.text)
    
    # Method to switch languages
    def switch_languages(self, source_combobox, dest_combobox):
        # Get the current index of the source and target language combo boxes
        source_index = source_combobox.currentIndex()
        dest_index = dest_combobox.currentIndex()
        # Set the current index of the source and target language combo boxes
        source_combobox.setCurrentIndex(dest_index)
        dest_combobox.setCurrentIndex(source_index)
           
    # Method to speak the text
    def speak_text(self):
        pass
    
    # Method to copy the text
    def copy_text(self):
        pass
    
    # Method to add to favorites
    def add_to_favorites(self):
        pass
    
    # Method to view history
    def view_history(self):
        pass
    
    # Method to view settings
    def view_settings(self):
        pass
 
# Run the application
if __name__ == "__main__":
    app = QApplication([])
    window = TranslatorApp()
    app.exec()