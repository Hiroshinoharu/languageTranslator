import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from googletrans import Translator,LANGUAGES

# A method to translate the text
def translate_text():
    # Getting the user input and the chosen languages
    src_text = text_input.get("1.0", tk.END).strip()
    src_lang = src_lang_var.get()
    dest_lang = dest_lang_var.get()
    
    # Translating the text
    translation = translator.translate(src_text, src=src_lang, dest=dest_lang)
    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, translation.text)


# A method to create the GUI
def create_gui():
    
    # Creating the main window
    window = tk.Tk()
    window.title("Translator")
    window.geometry("400x400")
    
    # Creating the translator object
    global translator
    translator = Translator()
    
    # Configuring the layout
    window.grid_columnconfigure(0, weight=1)
    window.grid_rowconfigure(0, weight=1)
    
    # Adding the logo
    logo = Image.open("images\logo.png")
    logo = ImageTk.PhotoImage(logo)
    
    # Creating the logo label
    logo_label = tk.Label(window,image=logo)
    logo_label.image = logo
    
    
    # Creating the input text box
    global text_input
    text_input = tk.Text(window,height=10, width=60)
    text_input.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
    
    # Language Selection for the source language
    tk.Label(window, text="Source Language").grid(row=1, column=0, padx=10, pady=10)
    global src_lang_var
    src_lang_var = tk.StringVar(window)
    src_lang_box = ttk.Combobox(window, textvariable=src_lang_var,values=list(LANGUAGES.values()), state="readonly")
    src_lang_box.grid(row=1, column=1, padx=10, pady=10)
    src_lang_box.set("english") # Setting the default language
    
    # Language Selection for the destination language
    tk.Label(window, text="Destination Language").grid(row=2, column=0, padx=10, pady=10)
    global dest_lang_var
    dest_lang_var = tk.StringVar(window)
    dest_lang_box = ttk.Combobox(window, textvariable=dest_lang_var,values=list(LANGUAGES.values()), state="readonly")
    dest_lang_box.grid(row=2, column=1, padx=10, pady=10)
    dest_lang_box.set("spanish") # Setting the default language
    
    #Translate button
    translate_button = tk.Button(window, text="Translate", command=translate_text)
    translate_button.grid(row=3, column=1, padx=10, pady=10,sticky="ew")
    
    # Translated text box
    global text_output
    text_output = tk.Text(window,height=10, width=60)
    text_output.grid(row=4, column=0, columnspan=3, padx=10, pady=10)
    
    # Running the main loop
    window.mainloop()


if __name__ == "__main__":
    create_gui()  
