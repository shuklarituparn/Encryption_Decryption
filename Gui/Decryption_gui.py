import customtkinter as ctk
from Encryption import caesar, vigenere, vernam
from tkinter import filedialog as fd


class Decryption_GUI(ctk.CTkToplevel):
    '''The Decryption GUI that decoded the text encoded when passed the file and the key path'''

    def __init__(self):
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.root = ctk.CTk()
        self.root.geometry("1000x1000")
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

        self.file_path_button = ctk.CTkButton(self.root, text="Choose the Encrypted path",
                                              command=self.get_file_path)
        self.file_path_button.pack(padx=10, pady=20)

        self.label_file_path_chosen = ctk.CTkLabel(self.root, font=("Arial", 10), text="",
                                                   anchor="center")
        self.label_file_path_chosen.pack(pady=10)

        self.label_key_path = ctk.CTkLabel(self.root, font=("Arial", 20), text="Enter the file path of the key",
                                           anchor="center")
        self.label_key_path.pack(pady=20)

        self.key_path_button = ctk.CTkButton(self.root, text="Choose the key for Decryption",
                                             command=self.get_key_path)
        self.key_path_button.pack(padx=10, pady=20)

        self.label_key_path_chosen = ctk.CTkLabel(self.root, font=("Arial", 10), text="",
                                                  anchor="center")
        self.label_key_path_chosen.pack(pady=10)

        self.start_button = ctk.CTkButton(self.root, text="Start the decryption", command=self.start_decryption)
        self.start_button.pack(padx=10, pady=20)

        self.label_output = ctk.CTkLabel(self.root, font=("Arial", 20), text="The output after decryption is",
                                         anchor="center")
        self.label_output.pack(pady=10)

        self.output_label = ctk.CTkTextbox(self.root)
        self.output_label.pack(pady=10)

        self.filepath = None
        self.keypath = None

    def get_file_path(self):
        self.filepath = fd.askopenfilename()
        self.label_file_path_chosen.configure(text=self.filepath)

        # The function is working

    def get_key_path(self):
        self.keypath= fd.askopenfilename()
        self.label_key_path_chosen.configure(text=self.keypath)
        # The function is working

    def start_decryption(self):

        file_to_decrypt = ''
        key_to_decrypt = ''

        with open(self.filepath, "r") as file1:
            file_to_decrypt = file1.read()

        with open(self.keypath, "r") as key:
            key_to_decrypt = key.read()

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
