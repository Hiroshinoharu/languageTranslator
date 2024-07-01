from gtts import gTTS
import pygame
import tempfile
import pyperclip

from googletrans import Translator, LANGUAGES  # Importing necessary libraries
from PyQt6.QtWidgets import QMessageBox  # Importing QMessageBox from PyQt6

class TranslatorLogic:
    def __init__(self):
        self.translator = Translator()  # Initializing the Translator object
    
    def translate_text(self, source_lang, dest_lang, text):
        if not text:  # Checking if the text is empty
            return "Please enter text to translate"  # Returning an error message
        result = self.translator.translate(text, src=self.get_lang_code(source_lang), dest=self.get_lang_code(dest_lang))  # Translating the text
        return result.text  # Returning the translated text
    
    def speak_text(self, text, lang):
        lang_code = self.get_lang_code(lang)  # Getting the language code
        try:
            tts = gTTS(text=text, lang=lang_code, slow=False)  # Creating a gTTS object for text-to-speech
            temp_file = tempfile.NamedTemporaryFile(delete=True)  # Creating a temporary file
            tts.save(temp_file.name + ".mp3")  # Saving the speech as an MP3 file
            pygame.mixer.init()  # Initializing the pygame mixer
            pygame.mixer.music.load(temp_file.name + ".mp3")  # Loading the MP3 file
            pygame.mixer.music.play()  # Playing the speech
            while pygame.mixer.music.get_busy():  # Waiting for the speech to finish playing
                continue
            temp_file.close()  # Closing the temporary file
        except Exception as e:
            print(f"Error occurred: {e}")  # Printing an error message if an exception occurs
    
    def copy_text(self, output_text):   
        # Copy the translated text to the clipboard
        pyperclip.copy(output_text)
        
        # Show a message box to indicate that the text has been copied
        msg = QMessageBox()  # Creating a QMessageBox object
        msg.setIcon(QMessageBox.Icon.Information)  # Setting the message icon
        msg.setText("Text copied to clipboard")  # Setting the message text
        msg.setWindowTitle("Copied")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()  # Executing the message box
    
    def add_to_favorites(self, text, translation, source_lang, dest_lang, favorites):
        num_items = len(favorites)  # Getting the number of items in the favorites list
        favorites[num_items + 1] = {self.get_lang_code(source_lang): text, self.get_lang_code(dest_lang): translation}  # Adding the translation to the favorites dictionary
    
    # Helper methods
    @staticmethod
    def get_languages():
        return LANGUAGES  # Returning the available languages
    
    # Helper method to get the language code given the language name
    @staticmethod
    def get_lang_code(lang):
        return [k for k, v in LANGUAGES.items() if v == lang][0]  # Returning the language code for the given language name
