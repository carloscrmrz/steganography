import sys
sys.path.append("..")
from operator import methodcaller

from model import decoder as dec
from model import binary_converter as bc
from model import encoder as enc
from PIL import Image
import numpy as snoopy

print("Aquí verificamos que al intentar abrir un archivo",
        "este, primero, sea una imagen y, segundo, sea PNG.\n")

archivos = ["panda.txt","perro.pdf","gato.png","pez.jpeg",
            "ballena.mp3", "ganso.mp4", "hiena.apk",
            "koala.png", "lobo.docx", "pingu.png"]

verdad = [False, False, True, True, False, False, False,
          True, False, True]

verdadaprueba = list()

for name in archivos:
    verdadaprueba.append(dec.comprobar(name))

for i in range (10):
    if (verdad[i] == verdadaprueba[i]):
        print ('\033[92m¡Éxito!\033[0m')
    else:
        print ('\033[93mFracaso\033[0m')

# print("Ahora verificamos que al extraer los bytes de la data del PNG",
#         " descartemos los primeros 8, pues los correspondientes a indicar",
#         " el formato PNG.\n")
#
# image1 = Image.open('gato.png')
# img1dataorig = snoopy.array(list(image1.getdata()))
# image2 = Image.open('koala.png')
# img2dataorig = snoopy.array(list(image2.getdata()))
# image3 = Image.open('pingu.png')
# img3dataorig = snoopy.array(list(image3.getdata()))
# print(img1dataorig)
# if (len(img1dataorig)-24 == len(dec.descartarBytesFormato(image1))):
#     print ('\033[92m¡Éxito!\033[0m')
# else:
#     print ('\033[93mFracaso\033[0m')
# if (len(img2dataorig)-24 == len(dec.descartarBytesFormato(image2))):
#     print ('\033[92m¡Éxito!\033[0m')
# else:
#     print ('\033[93mFracaso\033[0m')
#     if (len(img3dataorig)-24 == len(dec.descartarBytesFormato(image3))):
#         print ('\033[92m¡Éxito!\033[0m')
#     else:
#         print ('\033[93mFracaso\033[0m')

img = Image.open('pez.jpeg')
pixels1 = list(img.getdata())
#pixels2 = snoopy.array(list(img.getdata()))
#print(pixels1)
firstpix = pixels1[0]
#print(pixels2)
print(firstpix)

def suma(a,b):
    return a+b

tup = (2,2,2)

tup2 = tuple(map(bin,firstpix))
print(tup2)
print(tup2[0][2:])
x = int(tup2[0][2:])
print(type(x))
message_bits = []
for i in range (len(tup2)):
    message_bits.append(int(tup2[i][2:])%2)
print(message_bits)

pixeeels = []
for i in range (6):
    pixeeels.append(pixels1[i])

print(pixeeels)

print((pixeeels[0])[0])

message_bits2 = ""
for i in range (5):
    for j in range (3):
        message_bits2 += (str((pixeeels[i])[j]%2))
message_bits2 += str((pixeeels[5])[0]%2)
print(message_bits2)
message_bits2 = int(message_bits2,2)

print(message_bits2)
print(dec.get_length(pixeeels,3))

img4chan = Image.open('gato.png')
print(img4chan.mode)

img4chanpixels = list(img4chan.getdata())
morepixs = []
for i in range (4):
    morepixs.append(img4chanpixels[i])
messlength = ""
for i in range (4):
    for j in range (4):
        messlength += (str((morepixs[i])[j]%2))

print(messlength)
print(int(messlength,2))

print(dec.get_length(img4chanpixels,4))

def flatten_list_tup(ls):
    flat_ls = []
    for tup in ls:
        ls1 = []
        for item in tup:
            ls1.append(item)
        flat_ls.append(ls1)

    return flat_ls

print(pixeeels)

# yetmorepixs = ""
# print(len(img4chanpixels)*4)
# for i in range (4, 61165):
#     for j in range(4):
#         yetmorepixs += (str((img4chanpixels[i])[j]%2))
#
# # print(yetmorepixs) # <- should match what get_hidden_pixels returns
# yetmorepixs2 = dec.get_hidden_msg(img4chanpixels, 4)
# if (yetmorepixs == yetmorepixs2):
#     print ('\033[92m¡Éxito!\033[0m')
# else:
#     print ('\033[93mFracaso\033[0m')
# totespixs = ""
# totespixs += str((pixels1[5])[1]%2)
# totespixs += str((pixels1[5])[2]%2)
# for i in range (6, 50971):
#     for j in range(3):
#         totespixs += str((pixels1[i])[j]%2)
# totespixs2 = dec.get_hidden_msg(pixels1, 3)
# if (totespixs == totespixs2):
#     print ('\033[92m¡Éxito!\033[0m')
# else:
#     print ('\033[93mFracaso\033[0m')
# print(len(totespixs))
# print(len(totespixs2)) # <- should match what get_hidden_pixels returns
#
# encodedimg = Image.open('encoded.png')
# encodedpixs = list(encodedimg.getdata())
# fish = Image.open('pez.jpeg')
# fishpixs = list(fish.getdata())
#
# print(fishpixs[0])
# print(encodedpixs[0])

# channels = 0
# print(encodedimg.mode)
# if encodedimg.mode == 'RGBA':
#     channels = 4
# else:
#     channels = 3
# # encondedstringpixs = dec.get_hidden_pixels(encodedpixs, 4)
# # print(encondedstringpixs)
# for i in range (4, 12):
#     print(encodedpixs[i])
# print("a", dec.get_length(encodedpixs,4))
#
# encpixlength = []
# for i in range (4):
#     encpixlength.append(encodedpixs[i])
# print(encpixlength)
# encmesslength = ""
# for i in range (4):
#     for j in range (4):
#         encmesslength += (str((encpixlength[i])[j]%2))

enc = Image.open('encoded.png')
encpix = list(enc.getdata())
print(enc.mode)
channels = 3
if enc.mode == 'RGBA':
    channels =+ 1
print(dec.get_length(encpix,channels))
print(dec.get_hidden_msg(encpix,channels))

# pingu = Image.open('encoded2.png')
# pinguxels = list(pingu.getdata())
# print(pinguxels[0])
# print(pingu.mode)
# print(dec.get_length(pinguxels,4))
# print(dec.get_hidden_msg(pinguxels,4))
