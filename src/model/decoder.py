from PIL import Image
import model.binary_converter as bc

"""
    Función que obtiene la longitud de la cadena en binario
    que esconde el mensaje codificado. Recibe una lista de
    pixeles donde cada pixel es una tupla y una bandera que
    nos indica si son 3-tuplas o 4-tuplas, dependiendo del
    número de canales que tenga la imagen (3 para RGB y 4
    para RGBA).
"""
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

"""
    Función que obtiene los pixeles menos significativos
    de cada canal de cada pixel, los va agregando a
    hidden_message hasta que la longitud de dicha variable
    es del tamaño que get_length indicó. Hace la conversión
    de la cadena en binario a una cadena en texto plano
    para poder leerse por un humano.
"""
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
        if (hidden_message == "pato\n"):
            hidden_message = "¡El mensaje era ~pato~! ¡Encontraste al pato!"
        return hidden_message
    i = 4
    while len(hidden_message) < get_length(pixels, flag):
        for j in range(4):
            if len(hidden_message) < get_length(pixels, flag):
                hidden_message += (str((pixels[i])[j]%2))
        i += 1
    hidden_message = bc.decode_binary(hidden_message)
    if (hidden_message == "pato\n"):
        hidden_message = "¡El mensaje era ~pato~! ¡Encontraste al pato!"
    return hidden_message
