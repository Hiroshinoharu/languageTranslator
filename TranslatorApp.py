from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QComboBox, QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem, QMessageBox
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt
from googletrans import Translator, LANGUAGES # Import the required libraries
from gtts import gTTS
import pygame
import tempfile
import pyperclip

class TranslatorApp(QMainWindow):
    
    # Constructor
    def __init__(self):
        super().__init__()
        self.favorites = {1: {'Text': 'Hello', 'Transaltion': 'Hola'}, 2: {'Text': 'Bye', 'Translation': 'Adios'}}
        self.translator = Translator() # Create a translator object
        self.initUI() # Initialize the UI
     
    # Initialize the UI   
    def initUI(self):
        # Configure the main layout
        layout = QVBoxLayout() # Create a vertical layout
        
        #Variables set for icon buttons
        settings_icon = QPushButton("⚙️")
        history_icon = QPushButton("🕒") 
        
        # Star button actions
        star_icon = QPushButton("⭐")
        star_icon.clicked.connect(lambda: self.view_favorites()) # When the star icon is clicked, call the view_favorites method       
        
        # Header section
        header_icons = QHBoxLayout() # Create a horizontal layout
        spacer  = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum) # Create a spacer
        header_icons.addItem(spacer) # Add the spacer to the header
        
        # Adding icons to the top right of the GUI
        header_icons.addWidget(settings_icon) # Add the settings icon
        header_icons.addWidget(history_icon) # Add the history icon
        header_icons.addWidget(star_icon) # Add the favorites icon
        
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
        
        #Speaker button actions
        speaker_icon = QPushButton("🔊")
        speaker_icon.clicked.connect(lambda: self.speak_text(str(output_text.toPlainText()),dest_language_combobox.currentText())) # When the speaker icon is clicked, call the speak_text method
        
        # Copy button actions
        copy_icon = QPushButton("📋")
        copy_icon.clicked.connect(lambda: self.copy_text(str(output_text.toPlainText()))) # When the copy icon is clicked, call the copy_text method
        
        # Heart button actions
        heart_icon = QPushButton("❤️")
        heart_icon.clicked.connect(lambda: self.add_to_favorites(input_text.toPlainText(),output_text.toPlainText())) # When the heart icon is clicked, call the add_to_favorites method
        
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
    
    # Method to covert the langauge value to the language code
    def get_lang_code(self, lang):
        # Get the language code from the language value
        return [k for k, v in LANGUAGES.items() if v == lang][0]     
           
    # Method to speak the text
    def speak_text(self,text,lang):
        lang = self.get_lang_code(lang)
        try:
            # Create a text to speech object
            tts = gTTS(text=text, lang=lang, slow=False)
            # Save the audio to the temporary file
            temp_file = tempfile.NamedTemporaryFile(delete=True)
            tts.save(temp_file.name + ".mp3")
            # Initialize pygame mixer
            pygame.mixer.init()
            # Load the audio file
            pygame.mixer.music.load(temp_file.name + ".mp3")
            # Play the audio
            pygame.mixer.music.play()
            # Wait until the audio finishes playing
            while pygame.mixer.music.get_busy():
                continue
            # Clean up the temporary file
            temp_file.close()  
        except Exception as e:
            print(f"Error occurred: {e}")
    
    # Method to copy the text
    def copy_text(self,output_text):
        pyperclip.copy(output_text) # Copy the text to the clipboard
        # Show a message box to indicate that the text has been copied
        msg = QMessageBox(self) # Create a message box
        msg.setIcon(QMessageBox.Icon.Information) # Set the message icon
        msg.setText("Text copied to clipboard") # Set the message text
        msg.setWindowTitle("Copied")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()
        
    # Method to add to favorites
    def add_to_favorites(self, text, translation):
        # Get the number of items in the favorites dictionary
        num_items = len(self.favorites)
        # Add the text and translation to the favorites dictionary
        self.favorites[num_items + 1] = {'Text': text, 'Translation': translation}      
        # Show a message box to indicate that the text has been added to favorites
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setText("Text added to favorites")
        msg.setWindowTitle("Favorites")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()
        
    # Method to view favorites
    def view_favorites(self):
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