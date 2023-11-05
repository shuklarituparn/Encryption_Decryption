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


