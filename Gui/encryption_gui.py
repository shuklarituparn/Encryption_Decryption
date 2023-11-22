import os
import customtkinter as ctk
from Encryption import caesar, vigenere, vernam
from tkinter import filedialog as fd


class Encryption_GUI(ctk.CTkToplevel):
    '''Class that makes the Encryption GUI for our program'''

    def __init__(self):
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.root = ctk.CTk()
        self.root.geometry("1000x1000")
        self.root.title("The Encryption GUI")
        self.label_top = ctk.CTkLabel(self.root, font=("Arial", 34), text="Welcome to the Encryption Gui",
                                      anchor="center")
        self.label_top.pack(pady=20)
        self.label_method = ctk.CTkLabel(self.root, font=("Arial", 20), text="Choose the method to Encrypt",
                                         anchor="center")
        self.label_method.pack(pady=30)

        self.choice_var = ctk.StringVar()
        self.choice_button1 = ctk.CTkRadioButton(self.root, font=("Arial", 15), text="Encrypt using caesar",
                                                 variable=self.choice_var, value="Caeasr")
        self.choice_button1.pack(padx=10, pady=20)

        self.choice_button2 = ctk.CTkRadioButton(self.root, font=("Arial", 15), text="Encrypt using Vernam",
                                                 variable=self.choice_var, value="Vernam")
        self.choice_button2.pack(padx=10, pady=20)

        self.choice_button3 = ctk.CTkRadioButton(self.root, font=("Arial", 15), text="Encrypt using Vigenere",
                                                 variable=self.choice_var, value="Vigenere")
        self.choice_button3.pack(padx=10, pady=20)

        self.label_file_path = ctk.CTkLabel(self.root, font=("Arial", 20), text="Enter the file path of the text",
                                            anchor="center")
        self.label_file_path.pack(pady=20)

        self.file_path_button = ctk.CTkButton(self.root, text="Choose the file for Encryption",
                                              command=self.get_file_path)
        self.file_path_button.pack(padx=10, pady=20)

        self.label_file_path_chosen = ctk.CTkLabel(self.root, font=("Arial", 10), text="",
                                                  anchor="center")
        self.label_file_path_chosen.pack(pady=10)

        self.label_key_path = ctk.CTkLabel(self.root, font=("Arial", 20), text="Enter the file path of the key",
                                           anchor="center")
        self.label_key_path.pack(pady=20)

        self.key_path_button = ctk.CTkButton(self.root, text="Choose the key for Encryption",
                                             command=self.get_key_path)
        self.key_path_button.pack(padx=10, pady=20)

        self.label_key_path_chosen=ctk.CTkLabel(self.root, font=("Arial", 10), text="",
                                           anchor="center")
        self.label_key_path_chosen.pack(pady=10)

        self.start_button = ctk.CTkButton(self.root, text="Start the encryption", command=self.start_encryption)
        self.start_button.pack(padx=10, pady=20)

        self.label_output = ctk.CTkLabel(self.root, font=("Arial", 20), text="The output after encryption is",
                                         anchor="center")
        self.label_output.pack(pady=10)

        self.output_label = ctk.CTkTextbox(self.root)
        self.output_label.pack(pady=10)

        self.keypath = None
        self.filepath = None

    def get_file_path(self):
        self.filepath = fd.askopenfilename()
        self.label_file_path_chosen.configure(text=self.filepath)
        return self.filepath


    def get_key_path(self):
        self.keypath = fd.askopenfilename()
        self.label_key_path_chosen.configure(text=self.keypath)
        return self.keypath



    def start_encryption(self):
        '''Function that asks the user and calls the specified encryption method on the file and the key path passed'''
        file_to_encrypt=None
        key_to_use=None

        with open(self.filepath, "r") as file1:
            file_to_encrypt=file1.read()

        with open(self.keypath,"r") as key1:
            key_to_use=key1.read()

        choice_of_encryption = self.choice_var.get()
        if choice_of_encryption == "Caeasr":
            cipher = caesar.CaesarCipher(file_to_encrypt)
            encrypted_result = cipher.encrypt(file_to_encrypt, int(key_to_use))
            self.output_label.insert(index="0.0", text=encrypted_result)

        elif choice_of_encryption == "Vernam":
            cipher = vernam.VernamCipher(file_to_encrypt)
            encrypted_result = cipher.encrypt(file_to_encrypt, key_to_use)
            self.output_label.insert(index="0.0", text=encrypted_result)

        elif choice_of_encryption == "Vigenere":
            cipher = vigenere.VigenereCipher(file_to_encrypt)
            encrypted_result = cipher.encrypt(file_to_encrypt, key_to_use)
            self.output_label.insert(index="0.0", text=encrypted_result)


