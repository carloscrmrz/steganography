import sys
sys.path.append("..")

from src.deco import decoder as dec

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
        print ('\033[92m¡Éxito!')
    else:
        print ('\033[93mFracaso')
    print ('\033[0m')
