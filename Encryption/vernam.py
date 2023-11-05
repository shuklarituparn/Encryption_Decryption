class VernamCipher:
    def __init__(self, text):
        self.text = text  # this is the original text or the

    @staticmethod
    def read_text_from_file(file_path):
        with open(file_path, 'r') as file:
            return file.read()

    @staticmethod
    def read_key_from_file(key_path):
        with open(key_path, 'r') as file:
            return file.read()

    def encrypt(self, user_input: str, key_string: str) -> str:
        result = ""
        for i in range(len(user_input)):
            char = user_input[i]
            if char.isalpha():
                if char.isupper():
                    char_code = ord(char) - ord('A')
                    key_char = key_string[i].upper()
                    key_code = ord(key_char) - ord('A')
                    encrypted_char = char_code ^ key_code
                    if encrypted_char > 26:
                        encrypted_char = encrypted_char - 26
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

    def decrypt(self, encrypted_key: str, key_string: str) -> str:
        result = ""
        for i in range(len(encrypted_key)):
            char = encrypted_key[i]
            if char.isalpha():
                if char.isupper():
                    char_code = ord(char) - ord('A')
                    key_char = key_string[i].upper()
                    key_code = ord(key_char) - ord('A')
                    decrypted_char = char_code ^ key_code
                    if decrypted_char > 26:
                        decrypted_char = decrypted_char - 26
                        result += chr(decrypted_char + ord('A'))
                    else:
                        result += chr(decrypted_char + ord('A'))

                else:
                    char_code = ord(char) - ord('a')
                    key_char = key_string[i].lower()
                    key_code = ord(key_char) - ord('a')
                    decrypted_char = char_code ^ key_code
                    if decrypted_char > 26:
                        encrypted_char = 26 - decrypted_char
                        result += chr(decrypted_char + ord('a'))
                    else:
                        result += chr(decrypted_char + ord('a'))
            else:
                result += char

        return result


