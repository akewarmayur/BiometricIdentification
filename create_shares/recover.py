import random
from utils import Helper
from utils import SecretShare
_PRIME = 2**521 - 1
_BYTES = 65
_MINIMUM = 3
_SHARES = 10
def rec(Matrix):
	h = len(Matrix)
	shared_poly_index = []
	for i in range(0, _MINIMUM):
    		index = random.randint(1, _SHARES)
    		while index in shared_poly_index:
        		index = random.randint(1, _SHARES)
    		shared_poly_index.append(index)
	shared_poly_index.sort()


	recovered_stubs_int_list = []

	for i in range(0, h):
    		p_list = []
    		for j in range(0, len(shared_poly_index)):
        		p_list.append(Matrix[i][shared_poly_index[j]])
    		value = SecretShare.lagrange(0, shared_poly_index, p_list, _PRIME)

    		recovered_stubs_int_list.append(value)

	return recovered_stubs_int_list
	#img = Helper.create_image_from_int_list(recovered_stubs_int_list, _BYTES)
	#return img



