from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QComboBox, QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem, QMessageBox
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt
from FavoritesWindow import FavoritesWindow
from logic import TranslatorLogic
from utils import get_lang_code

class TranslatorApp(QMainWindow):
    favorites = {}

    def __init__(self):
        super().__init__()
        self.translator = TranslatorLogic()
        self.initUI()
     
    def initUI(self):
        layout = QVBoxLayout()
        
        settings_icon = QPushButton("⚙️")
        history_icon = QPushButton("🕒") 
        star_icon = QPushButton("⭐")
        star_icon.clicked.connect(lambda: self.view_favorites())
        
        header_icons = QHBoxLayout()
        spacer  = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        header_icons.addItem(spacer)
        header_icons.addWidget(settings_icon)
        header_icons.addWidget(history_icon)
        header_icons.addWidget(star_icon)
        
        image_label = QLabel()
        pixmap = QPixmap("images/logo.png")
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                
        language_selction_layout = QHBoxLayout()
        
        self.source_language_combobox = QComboBox()
        self.source_language_combobox.addItems(TranslatorLogic.get_languages().values())
        self.source_language_combobox.setCurrentText("english")
                       
        self.dest_language_combobox = QComboBox()
        self.dest_language_combobox.addItems(TranslatorLogic.get_languages().values())
        self.dest_language_combobox.setCurrentText("spanish")
        
        swap_language_button = QPushButton("🔄")
        swap_language_button.clicked.connect(self.switch_languages)
        
        language_selction_layout.addWidget(self.source_language_combobox)
        language_selction_layout.addWidget(swap_language_button)
        language_selction_layout.addWidget(self.dest_language_combobox)
        language_selction_layout.setSpacing(10)
        language_selction_layout.setContentsMargins(10, 10, 10, 10)
        
        text_area_layout = QHBoxLayout()
        
        self.input_text = QPlainTextEdit()
        self.input_text.setPlaceholderText("Enter text to translate...")
        
        self.output_text = QPlainTextEdit()
        self.output_text.setReadOnly(True)
        
        text_area_layout.addWidget(self.input_text)
        text_area_layout.addWidget(self.output_text)
        text_area_layout.setSpacing(10)
        text_area_layout.setContentsMargins(10, 10, 10, 10)
                
        textControlsLayout = QHBoxLayout()
        spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        textControlsLayout.addItem(spacer)
        
        translate_button = QPushButton("Translate")
        translate_button.clicked.connect(self.translate_text)
        
        speaker_icon = QPushButton("🔊")
        speaker_icon.clicked.connect(self.speak_text)
        
        copy_icon = QPushButton("📋")
        copy_icon.clicked.connect(self.copy_text)
        
        heart_icon = QPushButton("❤️")
        heart_icon.clicked.connect(self.add_to_favorites)
        
        textControlsLayout.addWidget(translate_button, 1, Qt.AlignmentFlag.AlignLeft)
        textControlsLayout.addWidget(speaker_icon)
        textControlsLayout.addWidget(copy_icon)
        textControlsLayout.addWidget(heart_icon)
        textControlsLayout.setSpacing(10)
        textControlsLayout.setContentsMargins(10, 10, 10, 10)
              
        layout.addLayout(header_icons)
        layout.addWidget(image_label)
        layout.addLayout(language_selction_layout)
        layout.addLayout(text_area_layout)
        layout.addLayout(textControlsLayout)
        
        main = QWidget()
        main.setLayout(layout)
        self.setCentralWidget(main)
        self.setWindowTitle("Lingualink Translator")
        self.setWindowIcon(QIcon("images/icon.png"))
        self.setFixedSize(714, 520)
        self.show()
    
    def translate_text(self):
        source_lang = self.source_language_combobox.currentText()
        dest_lang = self.dest_language_combobox.currentText()
        text = self.input_text.toPlainText()
        translation = self.translator.translate_text(source_lang, dest_lang, text)
        self.output_text.setPlainText(translation)
    
    def switch_languages(self):
        source_index = self.source_language_combobox.currentIndex()
        dest_index = self.dest_language_combobox.currentIndex()
        self.source_language_combobox.setCurrentIndex(dest_index)
        self.dest_language_combobox.setCurrentIndex(source_index)
    
    def speak_text(self):
        text = self.output_text.toPlainText()
        lang = self.dest_language_combobox.currentText()
        self.translator.speak_text(text, lang)
    
    def copy_text(self):
        output_text = self.output_text.toPlainText()
        self.translator.copy_text(output_text)
        
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
        
    def view_favorites(self):
        self.favorites_window = FavoritesWindow(self.favorites)
        self.favorites_window.show()
    
    def view_history(self):
        pass
    
    def view_settings(self):
        pass
