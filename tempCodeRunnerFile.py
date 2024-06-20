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