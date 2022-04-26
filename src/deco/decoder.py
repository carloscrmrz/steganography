from PIL import Image
import numpy as snoopy # Me gusta Snoopy

def comprobar(name):
    try:
        img = Image.open(name)
        t = (img.verify and (img.format == 'PNG' or img.format == 'JPEG'))
        return t
    except:
        t = False
        return t

# def descartarBytesFormato(img):
#     imgdata = snoopy.array(list(img.getdata()))
#     for i in range (24):
#         snoopy.delete(imgdata, 0)
#     return imgdata

def get_length(pixels, flag):
    hidden_message_length = ""
    if flag == 3:
        for i in range (5):
            for j in range (3):
                hidden_message_length += (str((pixels[i])[j]%2))
        hidden_message_length += str((pixels[5])[0]%2)
        hidden_message_length = int(hidden_message_length, 2)
        return hidden_message_length
    for i in range (4):
        for j in range (4):
            hidden_message_length += (str((pixels[i])[j]%2))
    hidden_message_length = int(hidden_message_length, 2)
    return hidden_message_length

def get_hidden_pixels(pixels, flag):
    hidden_message = ""
    if flag == 3:
        hidden_message += str((pixels[5])[1]%2)
        hidden_message += str((pixels[5])[2]%2)
        for i in range (6, (get_length(pixels, flag))-1):
            for j in range(3):
                hidden_message += (str((pixels[i])[j]%2))
        return hidden_message
    for i in range(4, (get_length(pixels, flag))-1):
        for j in range(4):
            hidden_message += (str((pixels[i])[j]%2))
    return hidden_message
