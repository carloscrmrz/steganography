from PIL import Image
import numpy as snoopy # Me gusta Snoopy

def comprobar(name):
    try:
        img = Image.open(name)
        t = (img.verify and (img.format == 'PNG'))
        return t
    except:
        t = False
        return t

def descartarBytesFormato(img):
    imgdata = snoopy.array(list(img.getdata()))
    for i in range (24):
        snoopy.delete(imgdata, 0)
    return imgdata
