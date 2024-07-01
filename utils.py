from googletrans import LANGUAGES

def get_lang_code(lang):
    return [k for k, v in LANGUAGES.items() if v == lang][0]
