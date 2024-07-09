# Lingualink: Language Translator App

## Overview
Lingualink is a language translator app designed to facilitate quick and efficient text translation. This project utilizes APIs such as PyQt6 for the user interface, googletrans for translation, pygame, and gtts for text-to-speech functionality.

## Project Structure
The project is divided into five modules to ensure code organization and modularity, with each module responsible for a specific functionality:

1. **main.py**
   - This module integrates all other modules to run the application.

2. **init_ui.py**
   - Responsible for providing an interface for the user to configure settings for translating text, switching languages, speaking the translated text, copying the translated text, adding translations to favorites, and viewing favorites.

3. **logic.py**
   - Provides the logic for translating text, speaking text, copying text, and managing favorites and history.

4. **FavoritesWindow.py**
   - Displays a list of favorite translations.

5. **HistoryWindow.py**
   - Displays a list of previous translations.

## Object-Oriented Principles
This project employs object-oriented principles such as encapsulation, inheritance, polymorphism, and abstraction to encourage code reuse, maintainability, and scalability. Classes and objects represent real-world entities and encapsulate related functionalities.

## Project Scopes
The goal of this project is to develop a functional language translator with basic functionalities and an intuitive UI. This project also aims to enhance understanding of API programming and dependency management, laying the groundwork for further learning in software development.

## Core Functionality
- Translate written text to any language.
- Text-to-speech functionality.

## Optional Functionality
- History window to access previous translations.
- Favorites function for quick access to preferred translations.
- Copy button for easy copying of translations.

## Future Improvements
- Improve the formatting of the favorites and history windows.
- Add functionality to remove specific translations from favorites.

## How to Run
1. Ensure you have Python installed on your system.
2. Install the required dependencies:
   ```
   pip install pyqt6 googletrans pygame gtts
   ```
3. Run the application:
   ```
   python main.py
   ```

## Dependencies
- PyQt6
- googletrans
- pygame
- gtts
