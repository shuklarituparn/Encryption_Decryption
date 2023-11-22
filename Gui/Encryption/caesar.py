from __future__ import annotations
from string import ascii_letters
import os


class CaesarCipher:

    def __init__(self, text):
        self.text = text

    def encrypt( self,input_string: str, key: int) -> str:
        alpha = ascii_letters

        result = ""

        for character in input_string:
            if character not in alpha:

                result += character
            else:
                new_key = (alpha.index(character) + key) % len(alpha)
                result += alpha[new_key]

        return result

    def decrypt(self,input_string: str, key: int) -> str:
        # Turn on decode mode by making the key negative

        result=""
        key *= -1
        alpha = ascii_letters

        result = ""

        for character in input_string:
            if character not in alpha:

                result += character
            else:
                new_key = (alpha.index(character) + key) % len(alpha)
                result += alpha[new_key]




        return  result





