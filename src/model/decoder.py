from PIL import Image
from . import binary_converter as bc

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

def get_hidden_msg(pixels, flag):
    hidden_message = ""
    if flag == 3:
        hidden_message += str((pixels[5])[1]%2)
        hidden_message += str((pixels[5])[2]%2)
        i = 6
        while len(hidden_message) < get_length(pixels, flag)-2:
            for j in range(3):
                if len(hidden_message) < get_length(pixels, flag)-2:
                    hidden_message += (str((pixels[i])[j]%2))
            i += 1
        hidden_message = bc.decode_binary(hidden_message)
        return hidden_message
    i = 4
    while len(hidden_message) < get_length(pixels, flag):
        for j in range(4):
            if len(hidden_message) < get_length(pixels, flag):
                hidden_message += (str((pixels[i])[j]%2))
        i += 1
    hidden_message = bc.decode_binary(hidden_message)
    return hidden_message
