import customtkinter as ctk
from Encryption import caesar, vigenere, vernam
import os


class Decryption_GUI(ctk.CTkToplevel):
    '''The Decryption GUI that decoded the text encoded when passed the file and the key path'''
    def __init__(self):
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.root = ctk.CTk()
        self.root.geometry("800x800")
        self.root.title("The Decryption GUI")
        self.label_top = ctk.CTkLabel(self.root, font=("Arial", 34), text="Welcome to the Decryption Gui",
                                      anchor="center")
        self.label_top.pack(pady=20)
        self.label_method = ctk.CTkLabel(self.root, font=("Arial", 20), text="Choose the method to Decrypt",
                                         anchor="center")
        self.label_method.pack(pady=30)

        self.choice_var = ctk.StringVar()
        self.choice_button1 = ctk.CTkRadioButton(self.root, font=("Arial", 15), text="Decrypt using caesar",
                                                 variable=self.choice_var, value="Caeasr")
        self.choice_button1.pack(padx=10, pady=20)

        self.choice_button2 = ctk.CTkRadioButton(self.root, font=("Arial", 15), text="Decrypt using Vernam",
                                                 variable=self.choice_var, value="Vernam")
        self.choice_button2.pack(padx=10, pady=20)

        self.choice_button3 = ctk.CTkRadioButton(self.root, font=("Arial", 15), text="Decrypt using Vigenere",
                                                 variable=self.choice_var, value="Vigenere")
        self.choice_button3.pack(padx=10, pady=20)

        self.label_file_path = ctk.CTkLabel(self.root, font=("Arial", 20), text="Enter the file path of the text",
                                            anchor="center")
        self.label_file_path.pack(pady=20)

        self.file_path = ctk.StringVar()
        self.file_path_button = ctk.CTkEntry(self.root, placeholder_text="File_Path",
                                             textvariable=self.file_path)
        self.file_path_button.pack(padx=10, pady=20)

        self.label_key_path = ctk.CTkLabel(self.root, font=("Arial", 20), text="Enter the file path of the key",
                                           anchor="center")
        self.label_key_path.pack(pady=20)

        self.key_path = ctk.StringVar()

        self.Key_path_button = ctk.CTkEntry(self.root, placeholder_text="File_Path",
                                            textvariable=self.key_path)
        self.Key_path_button.pack(padx=10, pady=20)

        self.start_button = ctk.CTkButton(self.root, text="Start the decryption", command=self.start_decryption)
        self.start_button.pack(padx=10, pady=20)

        self.label_output = ctk.CTkLabel(self.root, font=("Arial", 20), text="The output after decryption is",
                                         anchor="center")
        self.label_output.pack(pady=10)

        self.output_label = ctk.CTkTextbox(self.root)
        self.output_label.pack(pady=10)

    def start_decryption(self):

        encryption_folder_path = os.path.join('..', 'Encryption')
        file_path = self.file_path_button.get()
        key_path = self.Key_path_button.get()
        file_path = os.path.join(encryption_folder_path, file_path)
        key_path = os.path.join(encryption_folder_path, key_path)
        file_to_decrypt = ''
        key_to_decrypt = ''
        encrypted_result = ''
        # Check if the directory and files exist
        if os.path.exists(encryption_folder_path):
            with open(file_path, "r") as file1:
                file_to_decrypt = file1.read()
                # print("File Contents:", file_to_encrypt)

            with open(key_path, "r") as key1:
                key_to_decrypt = key1.read()
                # print("Key Contents:", key_to_encrypt)
        else:
            print("The specified directory does not exist:", encryption_folder_path)

        choice_of_decryption = self.choice_var.get()
        if choice_of_decryption == "Caeasr":
            cipher = caesar.CaesarCipher(file_to_decrypt)
            encrypted_result = cipher.decrypt(file_to_decrypt, int(key_to_decrypt))
            self.output_label.insert(index="0.0", text=encrypted_result)

        elif choice_of_decryption == "Vernam":
            cipher = vernam.VernamCipher(file_to_decrypt)
            encrypted_result = cipher.decrypt(file_to_decrypt, key_to_decrypt)
            self.output_label.insert(index="0.0", text=encrypted_result)

        elif choice_of_decryption == "Vigenere":
            print("hello from vigenere")
            cipher = vigenere.VigenereCipher(file_to_decrypt)
            encrypted_result = cipher.decrypt(file_to_decrypt, key_to_decrypt)
            self.output_label.insert(index="0.0", text=encrypted_result)
