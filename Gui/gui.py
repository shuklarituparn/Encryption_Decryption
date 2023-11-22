from PIL import Image, ImageTk
import customtkinter as ctk
import encryption_gui as egui
import Decryption_gui as dgui
import Steganography_gui as sgui


class EncryptionApp:
    '''The main Class that creates the Main Window of our GUI and from here all the other GUI are called'''
    def __init__(self):
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.root = ctk.CTk()
        self.root.geometry("400x400")
        self.root.title("The Encryption/Decryption program")

        self.label_top = ctk.CTkLabel(self.root, font=("Arial", 34), text="Choose your Mode")
        self.label_top.pack(pady=40)

        self.option_var = ctk.StringVar(value="Choose the Mode")

        self.drop = ctk.CTkOptionMenu(self.root, width=30, height=20, font=("Arial", 15),
                                      values=["Encryption", "Decryption", "Steganography"], variable=self.option_var)
        self.drop.pack(pady=20)

        self.button_text = ctk.StringVar()
        self.button1 = ctk.CTkButton(self.root, font=("Arial", 15), textvariable=self.button_text,
                                     command=self.openwindow)
        self.button1.pack(pady=20)

        def update_button_text(*args):
            '''Function that keeps track of the user choice and changes the button description bases on it'''
            selected_option = self.option_var.get()
            self.button_text.set("Open " + selected_option + " GUI")

        self.option_var.trace("w", update_button_text)
        self.root.mainloop()

    def openwindow(self):
        '''Function that opens the corresponding GUI window of the method that the user selected'''
        selected_option = self.option_var.get()
        if selected_option == "Encryption":
            self.toplevel_window = egui.Encryption_GUI()

        if selected_option == "Decryption":
            self.toplevel_window = dgui.Decryption_GUI()

        if selected_option == "Steganography":
            self.toplevel_window = sgui.Steganogrphy_GUI()


if __name__ == "__main__":
    app = EncryptionApp()
