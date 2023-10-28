from __future__ import annotations
from string import ascii_letters
import os


def calculate_frequencies(text, alphabet):
    frequency_count = {char: 0 for char in alphabet}

    for char in text:
        if char in alphabet:
            frequency_count[char] += 1

    return frequency_count


def encrypt(input_string: str, key: int, alphabet: str | None = None) -> str:
    alpha = alphabet or ascii_letters

    result = ""

    for character in input_string:
        if character not in alpha:

            result += character
        else:
            new_key = (alpha.index(character) + key) % len(alpha)
            result += alpha[new_key]

    return result


def vigenere_encrypt(input_string: str, key_string: str) -> str:
    result = ""

    # Ensure the key is repeated to match the length of the input_string
    key_repeated = key_string * (len(input_string) // len(key_string)) + key_string[
                                                                         :len(input_string) % len(key_string)]

    for i in range(len(input_string)):
        char = input_string[i]
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            is_upper = char.isupper()
            char = char.lower()

            # Shift the character by the corresponding key character
            char_code = ord(char) - ord('a')
            key_char = key_repeated[i]
            key_code = ord(key_char) - ord('a')
            encrypted_char = chr(((char_code + key_code) % 26) + ord('a'))

            # Restore the character to uppercase if it was originally uppercase
            if is_upper:
                encrypted_char = encrypted_char.upper()

            result += encrypted_char
        else:
            # If the character is not a letter, leave it unchanged
            result += char

    return result


def vernam_encrypt(input_string: str, key_string: str) -> str:
    result = ""
    for i in range(len(input_string)):
        char = input_string[i]
        if char.isalpha():
            if char.isupper():
                char_code = ord(char) - ord('A')
                key_char = key_string[i].upper()
                key_code = ord(key_char) - ord('A')
                encrypted_char = char_code ^ key_code
                if encrypted_char > 26:
                    encrypted_char = encrypted_char-26
                    result += chr(encrypted_char + ord('A'))
                else:
                    result += chr(encrypted_char + ord('A'))

            else:
                char_code = ord(char) - ord('a')
                key_char = key_string[i].lower()
                key_code = ord(key_char) - ord('a')
                encrypted_char = char_code ^ key_code
                if encrypted_char > 26:
                    encrypted_char = 26 - encrypted_char
                    result += chr(encrypted_char + ord('a'))
                else:
                    result += chr(encrypted_char + ord('a'))
        else:
            result += char

    return result


def decrypt(input_string: str, key: int, alphabet: str | None = None) -> str:
    # Turn on decode mode by making the key negative
    key *= -1

    return encrypt(input_string, key, alphabet)


def brute_force_with_frequency(input_string, alphabet=None):
    alpha = alphabet or ascii_letters
    brute_force_data = {}

    input_frequencies = calculate_frequencies(input_string, alpha)

    for key in range(1, len(alpha) + 1):
        # Decrypt the message
        decrypted_text = decrypt(input_string, key, alpha)

        # Calculate character frequencies in the decrypted text
        decrypted_frequencies = calculate_frequencies(decrypted_text, alpha)

        # Calculate the difference between input and decrypted frequencies
        frequency_diff = sum(abs(input_frequencies[char] - decrypted_frequencies[char]) for char in alpha)

        # Store the frequency difference as the "score" for this key
        brute_force_data[key] = frequency_diff

    # Find the key with the lowest score (most likely key)
    most_likely_key = min(brute_force_data, key=brute_force_data.get)

    return decrypt(input_string, most_likely_key, alpha)


if __name__ == "__main__":
    while True:
        print(f'\n{"-" * 10}\n Menu\n{"-" * 10}')
        print(*["1.Encrypt", "2.Decrypt", "3.Quit"], sep="\n")

        choice = input("\nWhat would you like to do?: ").strip() or "5"

        if choice not in ("1", "2", "3"):
            print("Invalid choice, please enter a valid choice")
        elif choice == "1":
            os.system('clear')
            print(f'\n{"-" * 10}\nChoose the Encryption Method:\n{"-" * 10}')
            print(*["1.Caesar", "2.Vigenere", "3.Vernam"], sep="\n")
            type_encryption = input().strip()
            if type_encryption not in ("1", "2", "3"):
                print("Invalid choice, please enter a valid choice")
            elif type_encryption == '1':
                os.system('clear')
                print("Encrypting using the Caesar Cipher: \n")
                print("Enter the string you want to encrypt: ")
                input_string = input().strip()
                key = int(input("Please enter off-set: ").strip())
                print(encrypt(input_string, key))

            elif type_encryption == '2':
                os.system("cls")
                print("Encrypting using the Vigenere Cipher: \n")
                print("Enter the string you want to encrypt: ")
                input_string = input().strip()
                print("Enter the key you want to encrypt with: ")
                key_string = input().strip()
                print(vigenere_encrypt(input_string, key_string))


            elif type_encryption == '3':
                os.system("cls")
                print("Encrypting using the Vernam Cipher: \n")
                print("Enter the string you want to encrypt: ")
                input_string = input().strip()
                print("Enter the key you want to encrypt with: ")
                key_string = input().strip()
                if len(key_string) != len(input_string):
                    print("Enter the key with the same length as the input text ")
                else:
                    print(vernam_encrypt(input_string, key_string))



        elif choice == "2":
            input_string = input("Please enter the string to be decrypted: ")
            key = int(input("Please enter off-set: ").strip())

            print(decrypt(input_string, key))
        elif choice == "3":
            input_string = input("Please enter the string to be decrypted: ")
            brute_force_data = brute_force_with_frequency(input_string)

            for key, value in brute_force_data.items():
                print(f"Key: {key} | Message: {value}")
        elif choice == "4":
            input_string = input("Please enter the string to be decrypted: ")
            decrypted_text = brute_force_with_frequency(input_string)
            print(f"Decrypted text (most likely): {decrypted_text}")
        elif choice == "5":
            print("Goodbye.")
            break
