# 🔎 Steganography

**Integrantes:**
- Cabrera Ramirez Carlos
- Medina Guzman Sergio (en mi rama, en el commit prepreúltimos ajustes, SHA 10c569c00ed317d107e7dcfbde1605d47c5244ed, está la carpeta test con pruebas que fueron ayudando a construir el código ;D)

**Proyecto 02** para la clase de **Modelado y Programacion** con el profesor Jose Galaviz, Ximena Lezama, Luis Soto y Karla Esquivel en la Facultad de Ciencias, UNAM.

**Steganography** es una aplicacion que permite esconder un mensaje de texto en una imagen, y a su vez obtener mensajes escondidos en imagenes previamente creadas con la aplicacion.

# 🔎 Uso Steganography

1. **Sistema Operativo:** Linux · Mac OS / OS X · Windows 10
2. **Version de Python:** Python 3.6+

### Prerrequisitos
Antes de instalar los modulos, asegurate que `pip3` este actualizado.

```
$ pip3 install pytest
$ pip3 install --upgrade Pillow
```

Para ejecutar las pruebas unitarias, nos situaremos en el directorio `src` y ejecutaremos el comando:
```
$ pytest
```

Para ejecutarse requerimos, una vez que hemos escrito en el archivo tth.txt (tth: text to hide) el mensaje que deseamos esconder, situarnos dentro del directorio `src`, hecho esto y con Pillow instalado usaremos el siguiente comando para esconder el mensaje dentro de tth.txt:
```
$ python3 steganography.py -e path/to/image.png tth.txt
```

Esto nos producira un archivo dentro de `src` llamado encoded.png, el cual es nuestra imagen con el mensaje codificado. Para decodificar y guardar el mensaje en un archivo txt con el nombre que deseemos usaremos el comando:
```
$ python3 steganography.py -e path/to/encoded.png nombredelarchivodeseado.txt
```

Este sacara a STDOUT el mensaje decodificado.

La aplicacion actualmente soporta los siguientes formatos de imagen:
- PNG
- JPEG
