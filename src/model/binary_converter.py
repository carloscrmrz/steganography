def encode_binary(string):
    return ''.join(format(ord(i),'b').zfill(8) for i in string)

def decode_binary(bin_string):
    decoded = ''
    for i in range(0, len(bin_string), 8):
        temp_str = bin_string[i:i+8]
        decoded = decoded + chr(int(temp_str,2))
    return decoded

