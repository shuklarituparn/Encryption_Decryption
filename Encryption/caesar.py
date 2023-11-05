from __future__ import annotations
from string import ascii_letters
import os


class CaesarCipher:

    def __init__(self, text):
        self.text = text

    @staticmethod
    def read_text_from_file(file_path):
        with open(file_path, 'r') as file:
            return file.read()

    @staticmethod
    def read_key_from_file(key_path):
        with open(key_path, 'r') as file:
            return file.read()

    def encrypt(self, input_string: str, key: int, alphabet: str | None = None) -> str:
        alpha = alphabet or ascii_letters

        result = ""

        for character in input_string:
            if character not in alpha:

                result += character
            else:
                new_key = (alpha.index(character) + key) % len(alpha)
                result += alpha[new_key]

        return result

    def decrypt(self,input_string: str, key: int, alphabet: str | None = None) -> str:
        # Turn on decode mode by making the key negative

        result=""
        key *= -1
        alpha = alphabet or ascii_letters

        result = ""

        for character in input_string:
            if character not in alpha:

                result += character
            else:
                new_key = (alpha.index(character) + key) % len(alpha)
                result += alpha[new_key]




        return  result





