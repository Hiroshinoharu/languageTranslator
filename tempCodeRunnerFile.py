import unittest
from unittest.mock import patch
from logic import TranslatorLogic

class TestTranslatorLogic(unittest.TestCase):
    def setUp(self):
        self.translator_logic = TranslatorLogic()

    @patch('logic.gTTS')
    @patch('logic.pygame')
    def test_speak_text(self, mock_pygame, mock_gTTS):
        # Mock the gTTS and pygame modules
        mock_gTTS_instance = mock_gTTS.return_value
        mock_pygame.mixer.music.get_busy.return_value = False

        # Call the speak_text method
        self.translator_logic.speak_text("Hello, world!", "en")

        # Assert that the gTTS constructor was called with the correct arguments
        mock_gTTS.assert_called_once_with(text="Hello, world!", lang="en", slow=False)

        # Assert that the gTTS save method was called with the correct argument
        mock_gTTS_instance.save.assert_called_once()

        # Assert that the pygame.mixer.music.load method was called with the correct argument
        mock_pygame.mixer.music.load.assert_called_once()

        # Assert that the pygame.mixer.music.play method was called
        mock_pygame.mixer.music.play.assert_called_once()

        # Assert that the pygame.mixer.music.get_busy method was called in a loop until it returns False
        mock_pygame.mixer.music.get_busy.assert_called()

        # Assert that the pygame.mixer.music.stop method was called
        mock_pygame.mixer.music.stop.assert_called_once()

        # Assert that the pygame.mixer.quit method was called
        mock_pygame.mixer.quit.assert_called_once()

if __name__ == "__main__":
    unittest.main()