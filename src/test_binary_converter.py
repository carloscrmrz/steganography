import model.binary_converter as conv

def test_encode_binary(message):
    return conv.encode_binary(message)

def test_decode_binary(bin_message):
    return conv.decode_binary(bin_message)


test_binary = \
  "011010000110010101101100011011000110111100100000011101110110111101110010011011000110010000001010"
test        = "hello world\n"

assert(test_encode_binary(test) == test_binary)
assert(test_decode_binary(test_binary) == test)
