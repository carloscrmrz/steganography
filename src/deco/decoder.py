from PIL import Image

def comprobar(name):
    try:
        img = Image.open(name)
        t = (img.verify and (img.format == 'PNG'))
        return t
    except:
        t = False
        return t
