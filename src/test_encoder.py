import model.encoder as encoder
import random
import queue

def comp_pixel(px1, px2):
    if ( px1 % 2 != px2 ):
        return px1 + 1
    return px1
    
def test_encode_rgb():
    """ 
    Test data, hello world is:
    Hexadecimal 68 65 6c 6c 6f 20 77 6f 72 6c 64 0a
    UTF-8       h  e  l  l  o     w  o  r  l  d  \n

    En binario se representaria:

    01101000 01100101 01101100 01101100 00100000 
    01110111 01101111 01110010 01101100 01100100 
    00001010

    """
    # Creamos nuestros datos como se pasaria en la aplicacion
    test        = "hello world"

    # La cadena en binario debe estar normalizada, ie debe ser multiplo de 3 o 4 
    # dependiendo si el modo es RGB o RGBA
    test_binary = \
      "0110100001100101011011000110110001101111001000000111011101101111011100100110110001100100"

    binary_array = [1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0]
    
    # Creamos una lista aleatoria de tuplas simulando cada uno un pixel RGB.
    test_pixels = \
      [(random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256)) for i in range(100)]

    test_pixels = encoder.encode_rgb(test, test_pixels)

    for i in range(0, len(test_pixels)-1):
        for j in range(0,3):
            assert(test_pixels[i][j] % 2 == binary_array.pop(0))
test_encode_rgb()
