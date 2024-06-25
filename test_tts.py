from gtts import gTTS
import os

def text_to_speech(text, lang):
    try:
        # Create a text to speech object
        tts = gTTS(text=text, lang=lang, slow=False)
        # Play the text to speech directly
        tts.save("output.mp3")
        os.system("start output.mp3")
    except Exception as e:
        print(f"Error occurred: {e}")

# Test the text_to_speech function
if __name__ == "__main__":
    text = "こんにちは、私はPythonを使っています。"
    lang = "ja"
    text_to_speech(text, lang)