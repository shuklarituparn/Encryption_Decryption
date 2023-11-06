from PIL import Image, ImageTk
import customtkinter as ctk
import tkinter as tk
import os


class EncryptionApp:
    def __init__(self):
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.root = ctk.CTk()
        self.root.geometry("800x800")
        self.root.title("The Encryption/Decryption program")

        label_top = ctk.CTkLabel(self.root, font=("Arial", 34), text="Choose your encryption")
        label_top.pack(pady=40)

        option_var=ctk.StringVar(value="Choose the Mode")

        drop=ctk.CTkOptionMenu(self.root,width=30,height=20, font=("Arial",15), values=["Encryption", "Decryption", "Steganography"], variable=option_var)
        drop.pack(pady=20)

        


        self.root.mainloop()


if __name__ == "__main__":
    app = EncryptionApp()
