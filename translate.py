import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Translator")
        self.translator = Translator()

        # Language selection
        self.src_lang = tk.StringVar(value="english")
        self.dest_lang = tk.StringVar(value="spanish")

        # Widgets
        self.create_widgets()

    def create_widgets(self):
        # Source Text
        self.src_label = ttk.Label(self.root, text="Source Text:")
        self.src_label.grid(row=0, column=0, padx=10, pady=10)
        self.src_text = tk.Text(self.root, height=10, width=50)
        self.src_text.grid(row=0, column=1, padx=10, pady=10)

        # Destination Text
        self.dest_label = ttk.Label(self.root, text="Translated Text:")
        self.dest_label.grid(row=1, column=0, padx=10, pady=10)
        self.dest_text = tk.Text(self.root, height=10, width=50, state='disabled')
        self.dest_text.grid(row=1, column=1, padx=10, pady=10)

        # Source Language Dropdown
        self.src_lang_label = ttk.Label(self.root, text="Source Language:")
        self.src_lang_label.grid(row=2, column=0, padx=10, pady=10)
        self.src_lang_combo = ttk.Combobox(self.root, textvariable=self.src_lang, values=list(LANGUAGES.values()))
        self.src_lang_combo.grid(row=2, column=1, padx=10, pady=10)

        # Destination Language Dropdown
        self.dest_lang_label = ttk.Label(self.root, text="Destination Language:")
        self.dest_lang_label.grid(row=3, column=0, padx=10, pady=10)
        self.dest_lang_combo = ttk.Combobox(self.root, textvariable=self.dest_lang, values=list(LANGUAGES.values()))
        self.dest_lang_combo.grid(row=3, column=1, padx=10, pady=10)

        # Translate Button
        self.translate_button = ttk.Button(self.root, text="Translate", command=self.translate_text)
        self.translate_button.grid(row=4, column=1, padx=10, pady=10)

    def translate_text(self):
        src_text = self.src_text.get("1.0", tk.END).strip()
        src_lang = self.get_lang_code(self.src_lang.get())
        dest_lang = self.get_lang_code(self.dest_lang.get())

        if not src_text:
            messagebox.showwarning("Input Error", "Please enter text to translate.")
            return

        try:
            translated = self.translator.translate(src_text, src=src_lang, dest=dest_lang)
            self.dest_text.config(state='normal')
            self.dest_text.delete("1.0", tk.END)
            self.dest_text.insert(tk.END, translated.text)
            self.dest_text.config(state='disabled')
        except Exception as e:
            messagebox.showerror("Translation Error", str(e))

    def get_lang_code(self, lang_name):
        for code, name in LANGUAGES.items():
            if name.lower() == lang_name.lower():
                return code
        return None

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()
