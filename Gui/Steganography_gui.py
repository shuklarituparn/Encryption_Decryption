import customtkinter as ctk
import os
from Encryption import caesar, vigenere, vernam, steganography


class Steganogrphy_GUI(ctk.CTkToplevel):
    '''Class that constructs the GUI for our steganography functions'''
    def __init__(self):
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.root = ctk.CTk()
        self.root.geometry("1000x1000")
        self.root.title("Welcome to the Steganography gui")

        self.Label_Welcome = ctk.CTkLabel(
            self.root, font=("Arial", 34), text="Welcome to the Steganography Gui "
        )
        self.Label_Welcome.pack(padx=10, pady=20)

        self.Label_filepath = ctk.CTkLabel(
            self.root, font=("Arial", 20), text="Enter the file path of the Image "
        )
        self.Label_filepath.pack(padx=10, pady=20)

        self.Image_path = ctk.StringVar()
        self.Image_path_button = ctk.CTkEntry(
            self.root, placeholder_text="File_Path", textvariable=self.Image_path
        )
        self.Image_path_button.pack(padx=10, pady=20)

        self.Label_Output_filepath = ctk.CTkLabel(
            self.root,
            font=("Arial", 20),
            text="Enter the output path of the Encoded " "Image ",
        )
        self.Label_Output_filepath.pack(padx=10, pady=20)

        self.Output_path = ctk.StringVar()
        self.Output_path_button = ctk.CTkEntry(
            self.root, placeholder_text="File_Path", textvariable=self.Output_path
        )
        self.Output_path_button.pack(padx=10, pady=20)

        self.Label_Message = ctk.CTkLabel(
            self.root, font=("Arial", 20), text="Enter the Message to Encrypt "
        )
        self.Label_Message.pack(padx=10, pady=20)

        self.Encrypt_Message = ctk.StringVar()
        self.Encrypt_Message_button = ctk.CTkEntry(
            self.root,
            placeholder_text="Message to be encrypted",
            textvariable=self.Encrypt_Message,
        )
        self.Encrypt_Message_button.pack(padx=10, pady=20)

        self.start_encoding_button = ctk.CTkButton(
            self.root, text="Start the encryption", command=self.start_encryption
        )
        self.start_encoding_button.pack(padx=10, pady=20)

        self.Label_Decrypted_Image = ctk.CTkLabel(
            self.root, font=("Arial", 17), text="Enter the File path of Encoded Image "
        )
        self.Label_Decrypted_Image.pack(padx=10, pady=20)

        self.Decrypt_Message = ctk.StringVar()
        self.Decrypt_Message_button = ctk.CTkEntry(
            self.root,
            placeholder_text="Message to be decrypted",
            textvariable=self.Decrypt_Message,
        )
        self.Decrypt_Message_button.pack(padx=10, pady=20)

        self.start_decoding_button = ctk.CTkButton(
            self.root, text="Start the decryption", command=self.start_decryption
        )
        self.start_decoding_button.pack(padx=10, pady=20)

        self.Label_Decrypted_text = ctk.CTkLabel(
            self.root, font=("Arial", 17), text="The Decrypted text is: "
        )
        self.Label_Decrypted_text.pack(padx=10, pady=20)

        self.output_label = ctk.CTkTextbox(self.root)
        self.output_label.pack(pady=10)

    def start_encryption(self):
        '''Function that calls the encryption method and passes the image path and the message to encrypt it'''
        encryption_folder_path = os.path.join("..", "Encryption")
        Image_file_path = self.Image_path_button.get()
        Message_to_encrypt = self.Encrypt_Message_button.get()
        file_path = os.path.join(encryption_folder_path, Image_file_path)
        cipher = steganography.ImageSteganography(image_path=Image_file_path)
        output_path_image = self.Output_path_button.get()
        cipher.encrypt(Message_to_encrypt, output_path_image)

    def start_decryption(self):
        '''Function that decrypts the data in the Image by taking the Encoded Image and decoding it'''
        encryption_folder_path = os.path.join("..", "Encryption")
        Encrypted_Image_file_path = self.Decrypt_Message_button.get()
        decrypted_message = ""
        file_path = os.path.join(encryption_folder_path, Encrypted_Image_file_path)
        cipher = steganography.ImageSteganography(image_path=file_path)
        decrypted_message = cipher.decrypt(Encrypted_Image_file_path)
        self.output_label.insert(index="0.0", text=decrypted_message)