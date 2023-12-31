class VigenereCipher:
    def __init__(self, text):
        self.text = text

    def encrypt(self, user_input, key_string) -> str:
        def generateKey(string, key):
            key = list(key)
            if len(string) == len(key):
                return (key)
            else:
                for i in range(len(string) -
                               len(key)):
                    key.append(key[i % len(key)])
            return ("".join(key))

        key_repeated1 = list(generateKey(user_input, key_string))


        result = ""

        for i in range(len(user_input)):
            char = user_input[i]

            if char.isalpha():
                is_upper = char.isupper()
                char = char.lower()
                key_char = key_repeated1[i].lower()
                key_code=ord(key_char)-ord('a')
                char_code=ord(char)-ord('a')
                encrypted_char= chr(((char_code+key_code)%26)+ord('a'))

                if is_upper:
                    encrypted_char = encrypted_char.upper()

                result += encrypted_char
            else:
                result += char

        return result

    def decrypt(self, user_input, key_string) -> str:
        def generateKey(string, key):
            key = list(key)
            if len(string) == len(key):
                return (key)
            else:
                for i in range(len(string) -
                               len(key)):
                    key.append(key[i % len(key)])
            return ("".join(key))

        key_repeated1 = list(generateKey(user_input, key_string))


        result = ""

        for i in range(len(user_input)):
            char = user_input[i]

            if char.isalpha():
                is_upper = char.isupper()
                char = char.lower()
                key_char = key_repeated1[i].lower()
                key_code = ord(key_char) - ord('a')
                char_code = ord(char) - ord('a')
                encrypted_char = chr(((char_code - key_code) % 26) + ord('a'))

                if is_upper:
                    encrypted_char = encrypted_char.upper()

                result += encrypted_char
            else:
                result += char

        return result


