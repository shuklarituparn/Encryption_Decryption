
# Encryption, Decryption, and Steganography Program

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

This program is a versatile tool for encrypting and decrypting data using three different encryption methods: Caesar, Vernam, and Vigenere. Additionally, it supports steganography, enabling you to hide encrypted data within an image.

## Getting Started

### Clone the Repository

```bash
git clone git@github.com:shuklarituparn/Encryption_Decryption.git

```

-Run the GUI Application
-Navigate to the gui directory and run the gui.py script.


```bash
cd Encryption_Decryption/gui
python gui.py
```
---

Select the Mode
- In the GUI window, select the mode you want to use: Encryption, Decryption, or Steganography. Press the corresponding button "Open" + mode + "Gui" (e.g., "Open Encryption Gui").

Choose Encryption Method
- If you selected the Encryption mode, you can choose from three encryption methods: Caesar, Vernam, or Vigenere. Select your preferred method using the radio buttons.

Input File and Key
- Provide the file path and key path in the respective fields.

Encrypt or Decrypt
- For encryption, click the "Encrypt" button.
- For decryption, go to the Decryption GUI, enter the encrypted file and the key, and click the "Decrypt" button. The result will be displayed in a text box in the GUI.

Steganography
- If you selected the Steganography mode, enter the image path and the message you want to encrypt.
- Click the "Start Encryption" button to hide the message within the image.
- To decrypt, enter the encrypted image path and click the "Start Decrypting" button. The decrypted text will be displayed in a text box.

## Supported Encryption Methods

### Caesar Cipher

The Caesar cipher is a simple substitution cipher that shifts each letter in the plaintext by a fixed number of positions down or up the alphabet.

### Vernam Cipher

The Vernam cipher, also known as the one-time pad, uses a random key of the same length as the plaintext to perform a bitwise XOR operation on the message, ensuring perfect secrecy when used correctly.

### Vigenere Cipher
The Vigenere cipher is a polyalphabetic substitution cipher that uses a keyword to shift each letter in the plaintext by varying positions in the alphabet.

## License

This program is open-source and available under the MIT License. Feel free to use, modify, and distribute it according to the terms of the license.

Please refer to the LICENSE file for more details.




