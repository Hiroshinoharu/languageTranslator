from googletrans import LANGUAGES

def get_lang_code(lang):
    """
    Get the language code for a given language.

    Parameters:
    lang (str): The language name.

    Returns:
    str: The language code corresponding to the given language.

    Raises:
    IndexError: If the given language is not found in the LANGUAGES dictionary.
    """
    return [k for k, v in LANGUAGES.items() if v == lang][0]

def get_languages():
    return LANGUAGES