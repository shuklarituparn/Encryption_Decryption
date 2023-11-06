import customtkinter as ctk

class Caesar_GUI(ctk.CTkToplevel):
    def __init__(self):
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.root = ctk.CTk()
        self.root.geometry("800x800")
        self.root.title("The Encryption/Decryption using Caesar")

