import model.binary_converter as bconv

def test_encode_binary(message):
    return bconv.encode_binary(message)

test_binary = \
  "011010000110010101101100011011000110111100100000011101110110111101110010011011000110010000001010"
test        = "hello world\n"

assert(test_encode_binary(test) == test_binary)
