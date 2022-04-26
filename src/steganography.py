import getopt, sys
from PIL import Image
import model.encoder as encoder
import model.decoder as decoder

def flatten_list_tup(ls):
    flat_ls = []
    for tup in ls:
        ls1 = []
        for item in tup:
            ls1.append(item)
        flat_ls.append(ls1)

    return flat_ls

def main():
    desc = "Steganography is a fast and easy way to hide messages in plain sight"
    args = sys.argv[1:]
    opts = "hd:e:"
    long_opts = ["--help", "--decode=", "--encode="]

    decode_encode_flag = ""
    path_to_img = ""
    message = ""
    try:
        arguments, values = getopt.getopt(args, opts, long_opts)
        for currentArg, currentVal in arguments:

            if currentArg in ("-h", "--help"):
                show_help()
            if currentArg in ("-d", "--decode"):
                decode_encode_flag = "decode"
                path_to_img = currentVal
            if currentArg in ("-e", "--encode"):
                decode_encode_flag = "encode"
                path_to_img = currentVal
                message = values[0]

    except getopt.error as err:
        print(str(err))

    if (decode_encode_flag == 'encode'):
        with Image.open(path_to_img) as img:
            pixels = list(img.getdata())
            if img.mode == "RGBA":
                new_pixels = encoder.encode_rgba(message, pixels)
            elif img.mode == "P":
                img = img.convert("RGBA")
                pixels = list(img.getdata())
                new_pixels = encoder.encode_rgba(message, pixels)
            else:
                new_pixels = encoder.encode_rgb(message, pixels)
            img.putdata(new_pixels)
            img.save("encoded.png")

    if (decode_encode_flag == 'decode'):
        with Image.open(path_to_img) as img:
            pixels = list(img.getdata())
            hidden_message = ""
            if img.mode == "RGBA":
                hidden_message = decoder.get_hidden_msg(pixels,4)
            elif img.mode == "RGB":
                hidden_message = decoder.get_hidden_msg(pixels,3)
            else:
                print("Esto no es un archivo valido")
            file = open("mensaje.txt", "w")
            file.write(hidden_message)
            file.close()

    # if (decode_encode_flag == 'decode'):
    #     with Image.open(path_to_img) as img:
    #         pixels = list(img.getdata())
    #         hidden_message = ""
    #         if img.mode == "RGBA":
    #             hidden_message = decoder.get_hidden_msg(pixels,4)
    #         elif img.mode == "RGB":
    #             hidden_message = decoder.get_hidden_msg(pixels,3)
    #         else:
    #             print("Esto no es un archivo valido")
    #         file = open("mensaje.txt", "w")
    #         file.write(hidden_message)
    #         file.close()


def show_help():
    print("Usage: steganography.py [-h|-d|-e]\n")
    print("arguments:")
    print("   -h, --help\t Shows this message and exits.")
    print("   -d, --decode\t Decodes a message from an image.")
    print("   -e, --encode\t Encodes a message in an image.")
    sys.exit(0)


main()
