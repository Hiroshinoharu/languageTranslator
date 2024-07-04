from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QComboBox, QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem, QMessageBox
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt
from FavoritesWindow import FavoritesWindow
from logic import TranslatorLogic


class TranslatorApp(QMainWindow): 
    """
    The main application window for the Lingualink Translator.

    This class represents the main window of the Lingualink Translator application. It provides the user interface
    for translating text, switching languages, speaking the translated text, copying the translated text, adding
    translations to favorites, and viewing favorites.

    Attributes:
        favorites (dict): A class variable dictionary to store favorites.

    Methods:
        __init__: Initializes the TranslatorApp object.
        initUI: Initializes the user interface.
        translate_text: Translates the input text.
        switch_languages: Switches the source and destination languages.
        speak_text: Speaks the translated text.
        copy_text: Copies the translated text to the clipboard.
        add_to_favorites: Adds the translation to favorites.
        view_favorites: Opens the favorites window.
        view_history: Opens the history window.
        view_settings: Opens the settings window.
    """
    
    # Define a class variable dictionary to store favorites
    favorites = {}
    
    # Define a class variable dictionary to store history
    history = {}

    # Define the constructor
    def __init__(self):
        super().__init__()
        self.translator = TranslatorLogic()
        self.initUI()
     
    # Define the method to initialize the user interface
    def initUI(self):
        # Create a vertical layout
        layout = QVBoxLayout()
        
        # Create buttons for settings and history
        settings_icon = QPushButton("⚙️")
        history_icon = QPushButton("🕒") 
        
        # Create a star icon button
        star_icon = QPushButton("⭐")
        star_icon.clicked.connect(lambda: self.view_favorites())
        
        # Create a horizontal layout for the header icons
        header_icons = QHBoxLayout()
        spacer  = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        header_icons.addItem(spacer)
        header_icons.addWidget(settings_icon)
        header_icons.addWidget(history_icon)
        header_icons.addWidget(star_icon)
        
        # Create a label for the image
        image_label = QLabel()
        pixmap = QPixmap("images/logo.png")
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                
        # Create a horizontal layout for the language selection
        language_selction_layout = QHBoxLayout()
        
        # Create a combo box for the source language
        self.source_language_combobox = QComboBox()
        self.source_language_combobox.addItems(TranslatorLogic.get_languages().values())
        self.source_language_combobox.setCurrentText("english")
                       
        # Create a combo box for the destination language
        self.dest_language_combobox = QComboBox()
        self.dest_language_combobox.addItems(TranslatorLogic.get_languages().values())
        self.dest_language_combobox.setCurrentText("spanish")
        
        # Create a button to swap the languages
        swap_language_button = QPushButton("🔄")
        swap_language_button.clicked.connect(self.switch_languages)
        
        # Add the widgets to the language selection layout
        language_selction_layout.addWidget(self.source_language_combobox)
        language_selction_layout.addWidget(swap_language_button)
        language_selction_layout.addWidget(self.dest_language_combobox)
        language_selction_layout.setSpacing(10)
        language_selction_layout.setContentsMargins(10, 10, 10, 10)
        
        # Create a horizontal layout for the text area
        text_area_layout = QHBoxLayout()
        
        # Create a plain text edit widget for input text
        self.input_text = QPlainTextEdit()
        self.input_text.setPlaceholderText("Enter text to translate...")
        
        # Create a plain text edit widget for output text
        self.output_text = QPlainTextEdit()
        self.output_text.setReadOnly(True)
        
        # Add the widgets to the text area layout
        text_area_layout.addWidget(self.input_text)
        text_area_layout.addWidget(self.output_text)
        text_area_layout.setSpacing(10)
        text_area_layout.setContentsMargins(10, 10, 10, 10)
                
        # Create a horizontal layout for the text controls
        textControlsLayout = QHBoxLayout()
        spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        textControlsLayout.addItem(spacer)
        
        # Create buttons for translate, speak, copy, and add to favorites
        translate_button = QPushButton("Translate")
        translate_button.clicked.connect(self.translate_text)
        
        speaker_icon = QPushButton("🔊")
        speaker_icon.clicked.connect(self.speak_text)
        
        copy_icon = QPushButton("📋")
        copy_icon.clicked.connect(self.copy_text)
        
        heart_icon = QPushButton("❤️")
        heart_icon.clicked.connect(self.add_to_favorites)
        
        # Add the buttons to the text controls layout
        textControlsLayout.addWidget(translate_button, 1, Qt.AlignmentFlag.AlignLeft)
        textControlsLayout.addWidget(speaker_icon)
        textControlsLayout.addWidget(copy_icon)
        textControlsLayout.addWidget(heart_icon)
        textControlsLayout.setSpacing(10)
        textControlsLayout.setContentsMargins(10, 10, 10, 10)
              
        # Add the layouts and widgets to the main layout
        layout.addLayout(header_icons)
        layout.addWidget(image_label)
        layout.addLayout(language_selction_layout)
        layout.addLayout(text_area_layout)
        layout.addLayout(textControlsLayout)
        
        # Create a main widget and set the layout
        main = QWidget()
        main.setLayout(layout)
        
        # Set the main widget as the central widget of the main window
        self.setCentralWidget(main)
        
        # Set the window title and icon
        self.setWindowTitle("Lingualink Translator")
        self.setWindowIcon(QIcon("images/icon.png"))
        
        # Set the fixed size of the main window
        self.setFixedSize(714, 520)
        
        # Show the main window
        self.show()
    
    # Define the method to translate the text
    def translate_text(self):
        source_lang = self.source_language_combobox.currentText()
        dest_lang = self.dest_language_combobox.currentText()
        text = self.input_text.toPlainText()
        translation = self.translator.translate_text(source_lang, dest_lang, text)
        self.output_text.setPlainText(translation)
    
    # Define the method to switch the languages
    def switch_languages(self):
        source_index = self.source_language_combobox.currentIndex()
        dest_index = self.dest_language_combobox.currentIndex()
        self.source_language_combobox.setCurrentIndex(dest_index)
        self.dest_language_combobox.setCurrentIndex(source_index)
    
    # Define the method to speak the text
    def speak_text(self):
        text = self.output_text.toPlainText()
        lang = self.dest_language_combobox.currentText()
        self.translator.speak_text(text, lang)
    
    # Define the method to copy the text
    def copy_text(self):
        output_text = self.output_text.toPlainText()
        self.translator.copy_text(output_text)
        
    # Define the method to add the text to favorites
    def add_to_favorites(self):
        text = self.input_text.toPlainText()
        translation = self.output_text.toPlainText()
        source_lang = self.source_language_combobox.currentText()
        dest_lang = self.dest_language_combobox.currentText()
        self.translator.add_to_favorites(text, translation, source_lang, dest_lang, self.favorites)
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setText("Text added to favorites")
        msg.setWindowTitle("Favorites")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()
        
    # Define the method to view the favorites window
    def view_favorites(self):
        self.favorites_window = FavoritesWindow(self.favorites)
        self.favorites_window.show()
    
    # Define the method to view the history
    def view_history(self):
        pass
    
    # Define the method to view the settings
    def view_settings(self):
        pass
