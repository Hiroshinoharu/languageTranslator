import os  # Importing the os library  
import pygame  # Importing the pygame library
import tempfile  # Importing the tempfile library
from gtts import gTTS  # Importing the gTTS library
from PyQt6.QtWidgets import QMessageBox
import pyperclip  # Importing QMessageBox from PyQt6
from googletrans import LANGUAGES, Translator # Importing the LANGUAGES dictionary from googletrans

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
            QMessageBox.critical(None, "Error", "Please enter text to speak")
            return
        
        lang_code = self.get_lang_code(lang)  # Getting the language code
        
        temp_file_path = ""  # Initialize temp_file_path with an empty string
        
        try:
            tts = gTTS(text=text, lang=lang_code, slow=False)
            
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
                temp_file_path = temp_file.name
                tts.save(temp_file_path)
                print(f"Temporary file created: {temp_file_path}")  # Log the creation of the temporary file
            
            # Check if the temporary file was created successfully
            if not os.path.exists(temp_file_path):
                print(f"Temporary file does not exist: {temp_file_path}")
                return

            # Verify the content of the temporary file
            file_size = os.path.getsize(temp_file_path)
            if file_size == 0:
                print(f"Temporary file is empty: {temp_file_path}")
                return
            
            print(f"Temporary file size: {file_size} bytes")
            
            # Initialize pygame mixer
            pygame.mixer.init()
            print("Pygame mixer initialized")
            
            # Load and play the audio file
            pygame.mixer.music.load(temp_file_path)
            print("Audio file loaded into pygame mixer")
            pygame.mixer.music.play()
            print("Playing audio")

            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
            
            print("Audio playback finished")
            pygame.mixer.music.stop()
            pygame.mixer.quit()
        except Exception as e:
            print(f"Error occurred: {e}")  # Printing an error message if an exception occurs
        finally:
            # Clean up the temporary file
            if os.path.exists(temp_file_path):
                try:
                    os.remove(temp_file_path)
                    print(f"Temporary file deleted: {temp_file_path}")  # Log the deletion of the temporary file
                except Exception as e:
                    print(f"Error deleting temporary file: {e}")
                    try:
                        os.remove(temp_file_path)
                        print(f"Temporary file deleted: {temp_file_path}")  # Log the deletion of the temporary file
                    except Exception as e:
                        print(f"Error deleting temporary file: {e}")

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
        history[num_items + 1] = {source_lang: text, dest_lang: translation}  # Adding the translation to the history dictionary
    
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
