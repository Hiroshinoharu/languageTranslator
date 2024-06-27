from gtts import gTTS
import pygame
import tempfile

def text_to_speech(text, lang):
    try:
        # Create a text to speech object
        tts = gTTS(text=text, lang=lang, slow=False)
        
        # Save the audio to a temporary file
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

# Test the text_to_speech function
if __name__ == "__main__":
    text = "Hola, ¿cómo estás?"
    lang = "es"
    text_to_speech(text, lang)