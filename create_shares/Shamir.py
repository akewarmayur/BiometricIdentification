import random
from utils import Helper
from utils import SecretShare

_PRIME = 2**521 - 1
_BYTES = 65
_MINIMUM = 3
_SHARES = 10
def generate_shares(file):
    image_bytes = file
    

    image_byte_array = bytearray(image_bytes)

    length = len(image_byte_array)


    stubs = int(length / _BYTES) + 1


    stubs_int_list = []

    counter = 0
    for i in range(0, int(length / _BYTES)):
        _bytes = image_byte_array[counter: counter + _BYTES]
        stubs_int_list.append(int.from_bytes(_bytes, byteorder='little'))
        counter = counter + _BYTES

    stubs_int_list.append(int.from_bytes(image_byte_array[counter: length], byteorder='little'))

#print(stubs_int_list)

# generate shares

    w = _SHARES + 1
    h = len(stubs_int_list)

    Matrix = [[0 for x in range(w)] for y in range(h)]

    for i in range(0, len(stubs_int_list)):
        list_of_coefficients = SecretShare.create_random_coefficients(_MINIMUM, _PRIME)

    # evaluate all the shares wrt this int
        for j in range(0, _SHARES + 1):
            Matrix[i][j] = SecretShare.evaluate_modulus_poly(stubs_int_list[i], list_of_coefficients, j, _PRIME)

    
    return Matrix
# Matrix is the secret; any _MINIMUM value pairs can be distributed

# recover the values
