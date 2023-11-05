import tkinter as tk
from tkinter import filedialog
import caesar
import vigenere
import vernam
import steganography

class EncryptionApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Encryption Program")
        self.geometry("800x800")
        self.selected_cipher = tk.StringVar()
        self.create_gui_elements()


