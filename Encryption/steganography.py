import numpy as np
from PIL import Image

class ImageSteganography:

    def __init__(self, image_path):
        self.image_path = image_path
        self.end_marker = "<END>"

    def encrypt(self, message, output_path):
        message += self.end_marker

        b_message = ''.join(["{:08b}".format(ord(x)) for x in message])
        b_message = [int(x) for x in b_message]
        b_message_length = len(b_message)

        with Image.open(self.image_path) as img:
            width, height = img.size
            data = np.array(img)

        data = np.reshape(data, -1)
        data[:b_message_length] = (data[:b_message_length] & ~1) | b_message
        data = np.reshape(data, (height, width, 3))

        new_img = Image.fromarray(data)
        new_img.save(output_path)
        new_img.show()

    def decrypt(self, secret_image_path):
        with Image.open(secret_image_path) as img:
            width, height = img.size
            data = np.array(img)

        data = np.reshape(data, width * height * 3)
        data = data & 1
        data = np.packbits(data)

        decoded_message = ""
        end_marker_index = 0

        for x in data:
            l = chr(x)
            decoded_message += l

            # Check for the end marker
            if l == self.end_marker[end_marker_index]:
                end_marker_index += 1
                if end_marker_index == len(self.end_marker):
                    break
            else:
                end_marker_index = 0

        return decoded_message[:-len(self.end_marker)]


