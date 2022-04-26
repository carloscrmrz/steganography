import array as arr
import model.binary_converter as bc

"""
 Funcion auxiliar para cambiar el bit menos significativo de cada valor de color.
 Recibe, el valor del pixel, determina si el bit menos significativo es igual al 
 bit requerido, si no lo es lo cambia.
 Su uso es dentro de una map() para crear una tupla nueva.
"""
def lsb_manager(px1, bit):
    if (px1 % 2 != bit):
        return px1 + 1
    return px1

"""
  Funcion para codificar un mensaje en binario en 
  una matriz de pixeles, esta funcion trabaja con 
  pixeles RGB, y por ende crea 3-tuplas.
"""
def encode_rgb(message, pixels):
    binary_message = bc.encode_binary(message, 3)
    binary_length  = bin(len(binary_message))[2:]
    binary_q       = arr.array('b', [])

    ## Hacemos esto para cuando hagamos la decodificacion sea sencillo conocer 
    ## el tamano del mensaje que queremos decodificar.
    for b in binary_length:
        binary_q.append(int(b))

    for b in binary_message:
        binary_q.append(int(b))

    newPixels = []
    for i in range(0, len(pixels) - 1):
        try:
            bits = (binary_q.pop(0), binary_q.pop(0), binary_q.pop(0))
            newPixels.append(tuple(map(lsb_manager, pixels[i], bits)))

        except IndexError:
            break

    return newPixels
"""
  Funcion para codificar un mensaje en binario en 
  una matriz de pixeles, esta funcion trabaja con 
  pixeles RGBA, y por ende crea 4-tuplas.
"""
def encode_rgba(message, pixels):
    binary_message = bc.encode_binary(message, 4)
    binary_length  = bin(len(binary_message))[2:]
    binary_q       = arr.array('b', [])

    ## Hacemos esto para cuando hagamos la decodificacion sea sencillo conocer 
    ## el tamano del mensaje que queremos decodificar.
    for b in binary_length:
        binary_q.append(int(b))

    for b in binary_message:
        binary_q.append(int(b))

    newPixels = []
    for i in range(0, len(pixels) - 1):
        try:
            bits = (binary_q.pop(0), binary_q.pop(0), binary_q.pop(0), binary_q.pop(0))
            newPixels.append(tuple(map(lsb_manager, pixels[i], bits)))

        except IndexError:
            break
    return newPixels
