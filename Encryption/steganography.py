import numpy as np
from PIL import Image

message = input("Enter the word you wanna encrypt: ")

# Encode the message in a serie of 8-bit values
b_message = ''.join(["{:08b}".format(ord(x)) for x in message])
b_message = [int(x) for x in b_message]

b_message_lenght = len(b_message)

# Get the image pixel arrays
with Image.open("img.png") as img:
    width, height = img.size
    data = np.array(img)

# Flatten the pixel arrays
data = np.reshape(data, -1)

# Overwrite pixel LSB
data[:b_message_lenght] = (data[:b_message_lenght] & ~1) | b_message

# Reshape back to an image pixel array
data = np.reshape(data, (height, width, 3))

new_img = Image.fromarray(data)
new_img.save("cover-secret.png")
new_img.show()

with Image.open("cover-secret.png") as img:
    width, height = img.size
    data = np.array(img)

data = np.reshape(data, width * height * 3)
# extract lsb
data = data & 1
# Packs binary-valued array into 8-bits array.
data = np.packbits(data)
# Read and convert integer to Unicode characters until hitting a non-printable character
# Read and convert integers to Unicode characters until reaching the end of the message
decoded_message = ""
for x in data:
    l = chr(x)
    if l == '\0':
        break
    decoded_message += l

print(decoded_message)




'''
/usr/bin/python3.10 /home/rituparn/Documents/Dev/languages/Proj1/Encryption/steganography.py 
Enter the word you wanna encrypt: m
mm¶Ûm¶ÿÿÿÿÿÿÿÿÿÿÿÿ¶ÛmI$
Process finished with exit code 0
'''