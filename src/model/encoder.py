import queue

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

def encode_rgb(message, pixels):
    binary_message = convert_binary(message)
    binary_q       = queue.SimpleQueue()

    for b in binary_message:
        binary_q.put(int(b))

    for i in range(0, len(pixels)):
        try:
            bits = (binary_q.get_nowait(), binary_q.get_nowait(), binary_q.get_nowait())
            pixel = pixels[i]
            newPixel = tuple(map(lsb_manager, pixel, bits))

            if ( newPx != pixel ):
                pixel = newPixel
        except queue.Empty:
            break

