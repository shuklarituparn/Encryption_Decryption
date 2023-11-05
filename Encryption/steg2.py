from PIL import Image
import numpy as np

# Open the image
img = Image.open('img.png')
img_data = np.array(img)

# Get the dimensions of the image
height, width, channels = img_data.shape

message = input("Enter the message to encrypt: ")
message_to_encrypt = ''.join(["{:08b}".format(ord(x)) for x in message])

# Make sure the message length is not longer than the number of pixels
if len(message_to_encrypt) > height * width * channels:
    print("Message is too long to encrypt in the image.")
    exit(1)

# Encrypt the message
message_idx = 0
for i in range(height):
    for j in range(width):
        for k in range(channels):
            if message_idx < len(message_to_encrypt):
                img_data[i, j, k] = (img_data[i, j, k] & 254) | int(message_to_encrypt[message_idx])
                message_idx += 1

# Save the encrypted image
encrypted_img = Image.fromarray(img_data)
encrypted_img.save('output.png')

# Open the image

img = Image.open('output.png')
img_data = np.array(img)

# Get the dimensions of the image
height, width, channels = img_data.shape

data = np.reshape(img_data, height * width * channels)

data=data&1
data=np.packbits(data)

text=''

for x in data:
    z=chr(x)
    if z.isprintable() is False:
        break
    text+=z

print(text)