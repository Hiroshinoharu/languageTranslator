from googletrans import Translator, LANGUAGES
from gtts import gTTS
import pygame
import tempfile
import pyperclip
from PyQt6.QtWidgets import QMessageBox

class TranslatorLogic:
    def __init__(self):
        self.translator = Translator()
    
    def translate_text(self, source_lang, dest_lang, text):
        if not text:
            return "Please enter text to translate"
        result = self.translator.translate(text, src=self.get_lang_code(source_lang), dest=self.get_lang_code(dest_lang))
        return result.text
    
    def speak_text(self, text, lang):
        lang_code = self.get_lang_code(lang)
        try:
            tts = gTTS(text=text, lang=lang_code, slow=False)
            temp_file = tempfile.NamedTemporaryFile(delete=True)
            tts.save(temp_file.name + ".mp3")
            pygame.mixer.init()
            pygame.mixer.music.load(temp_file.name + ".mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                continue
            temp_file.close()
        except Exception as e:
            print(f"Error occurred: {e}")
    
    def copy_text(self, output_text):   
        # Copy the translated text to the clipboard
        pyperclip.copy(output_text)
        
        # Show a message box to indicate that the text has been copied
        msg = QMessageBox() # Create a message box
        msg.setIcon(QMessageBox.Icon.Information) # Set the message icon
        msg.setText("Text copied to clipboard") # Set the message text
        msg.setWindowTitle("Copied")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()
    
    def add_to_favorites(self, text, translation, source_lang, dest_lang, favorites):
        num_items = len(favorites)
        favorites[num_items + 1] = {self.get_lang_code(source_lang): text, self.get_lang_code(dest_lang): translation}
    
    # Helper methods
    @staticmethod
    def get_languages():
        return LANGUAGES
    
    # Helper method to get the language codegiven the language name
    @staticmethod
    def get_lang_code(lang):
        return [k for k, v in LANGUAGES.items() if v == lang][0]