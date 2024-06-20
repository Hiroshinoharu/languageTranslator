from googletrans import Translator

translator = Translator()

def translate_text(text, src_lang = 'auto', dest_lang = 'en'):
    try:
        translation = translator.translate(text, src=src_lang, dest=dest_lang)
        return translation.text
    except Exception as e:
        return str(e)
    

if __name__ == '__main__':
    text_to_translate = "Hola, ¿cómo estás?"
    translated_text = translate_text(text_to_translate)
    print(f"Original text: {text_to_translate}")
    print(f"Translated text: {translated_text}")