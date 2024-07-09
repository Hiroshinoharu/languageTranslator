from gtts import gTTS # Importing the gTTS library
import pygame # Importing the pygame library
import tempfile # Importing the tempfile library
import pyperclip # Importing the pyperclip library

from googletrans import Translator, LANGUAGES  # Importing necessary libraries
from PyQt6.QtWidgets import QMessageBox  # Importing QMessageBox from PyQt6

class TranslatorLogic:
    """
    A class that provides logic for translating text, speaking text, copying text, and managing favorites and history.
    """

    def __init__(self):
        self.translator = Translator()  # Initializing the Translator object
    
    def translate_text(self, source_lang, dest_lang, text):
        """
        Translates the given text from the source language to the destination language.

        Args:
            source_lang (str): The source language.
            dest_lang (str): The destination language.
            text (str): The text to be translated.

        Returns:
            str: The translated text.
        """
        if not text:  # Checking if the text is empty
            return "Please enter text to translate"  # Returning an error message
        result = self.translator.translate(text, src=self.get_lang_code(source_lang), dest=self.get_lang_code(dest_lang))  # Translating the text
        return result.text  # Returning the translated text
    
    def speak_text(self, text, lang):
        """
        Speaks the given text in the specified language.

        Args:
            text (str): The text to be spoken.
            lang (str): The language of the text.
        """
        # Check if the text is empty
        if text == "":
            QMessageBox.critical(None, "Error", "Please enter text to speak")  # Displaying an error message if the text is empty
            return
        
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
        """
        Copies the translated text to the clipboard.

        Args:
            output_text (str): The translated text.
        """
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
        """
        Adds the translation to the favorites dictionary.

        Args:
            text (str): The original text.
            translation (str): The translated text.
            source_lang (str): The source language.
            dest_lang (str): The destination language.
            favorites (dict): The favorites dictionary.
        """
        num_items = len(favorites)  # Getting the number of items in the favorites list
        favorites[num_items + 1] = {source_lang: text, dest_lang: translation}  # Adding the translation to the favorites dictionary
        
    def add_to_history(self, text, translation, source_lang, dest_lang, history):
        """
        Adds the translation to the history dictionary.

        Args:
            text (str): The original text.
            translation (str): The translated text.
            source_lang (str): The source language.
            dest_lang (str): The destination language.
            history (dict): The history dictionary.
        """
        num_items = len(history)  # Getting the number of items in the history list
        history[num_items + 1] = {source_lang: text, dest_lang: translation} # Adding the translation to the history dictionary
    
    # Helper methods
    @staticmethod
    def get_languages():
        """
        Returns the available languages.

        Returns:
            dict: A dictionary of available languages.
        """
        return LANGUAGES  # Returning the available languages
    
    # Helper method to get the language code given the language name
    @staticmethod
    def get_lang_code(lang):
        """
        Returns the language code for the given language name.

        Args:
            lang (str): The language name.

        Returns:
            str: The language code.
        """
        return [k for k, v in LANGUAGES.items() if v == lang][0]  # Returning the language code for the given language name
