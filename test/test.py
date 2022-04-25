import sys
sys.path.append("..")

from src.deco import decoder as dec
from PIL import Image
import numpy as snoopy

print("Aquí verificamos que al intentar abrir un archivo",
        "este, primero, sea una imagen y, segundo, sea PNG.\n")

archivos = ["panda.txt","perro.pdf","gato.png","pez.jpg",
            "ballena.mp3", "ganso.mp4", "hiena.apk",
            "koala.png", "lobo.docx", "pingu.png"]

verdad = [False, False, True, False, False, False, False,
          True, False, True]

verdadaprueba = list()

for name in archivos:
    verdadaprueba.append(dec.comprobar(name))

for i in range (10):
    if (verdad[i] == verdadaprueba[i]):
        print ('\033[92m¡Éxito!\033[0m')
    else:
        print ('\033[93mFracaso\033[0m')

print("Ahora verificamos que al extraer los bytes de la data del PNG",
        " descartemos los primeros 8, pues los correspondientes a indicar",
        " el formato PNG.\n")

image1 = Image.open('gato.png')
img1dataorig = snoopy.array(list(image1.getdata()))
image2 = Image.open('koala.png')
img2dataorig = snoopy.array(list(image2.getdata()))
image3 = Image.open('pingu.png')
img3dataorig = snoopy.array(list(image3.getdata()))
print(img1dataorig)
if (len(img1dataorig)-24 == len(dec.descartarBytesFormato(image1))):
    print ('\033[92m¡Éxito!\033[0m')
else:
    print ('\033[93mFracaso\033[0m')
if (len(img2dataorig)-24 == len(dec.descartarBytesFormato(image2))):
    print ('\033[92m¡Éxito!\033[0m')
else:
    print ('\033[93mFracaso\033[0m')
    if (len(img3dataorig)-24 == len(dec.descartarBytesFormato(image3))):
        print ('\033[92m¡Éxito!\033[0m')
    else:
        print ('\033[93mFracaso\033[0m')
