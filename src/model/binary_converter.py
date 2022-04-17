"""
  Funcion que convierte una cadena de texto a su 
  representacion binaria en UTF-8, ademas de que normaliza
  la longitud de la cadena.
  Recibe ademas una bandera para la normalizacion de la 
  cadena de texto.
"""
def encode_binary(string, flag):
    binary = ''.join(format(ord(i),'b').zfill(8) for i in string)
    return normalize_string(binary,flag)

"""
  Funcion que permite convertir una cadena en binario a 
  su representacion en UTF-8
"""
def decode_binary(bin_string):
    decoded = ''
    for i in range(0, len(bin_string), 8):
        temp_str = bin_string[i:i+8]
        decoded = decoded + chr(int(temp_str,2))
    return decoded

"""
  Funcion para normalizar la longitud del mensaje. Recibe
  una cadena de longitud arbitraria, y dependiendo de la 
  bandera la convierte en una cadena de longitud de la cadena.
"""

def normalize_string(string, flag):
    return string + '0'*(flag - len(string) % flag)

