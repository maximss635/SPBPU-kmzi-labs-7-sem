from params import *


def bytes_to_integer(block, count):
    if count == 4:
        return (block[0] << 24) | (block[1] << 16) | (block[2] << 8) | block[3]
    elif count == 3:
        return (block[0] << 16) | (block[1] << 8) | block[2]
    elif count == 2:
        return (block[0] << 8) | block[1]
    else:
        return block[0]


# One round only!
class SPNetwork:
    def __init__(self, params):
        self._params = params

    def convert_block(self, block, key):
        #assert(isinstance(block, int))
        #assert(isinstance(key, int))

        block ^= key
        block = self.__s(block)
        block = self.__p(block)

        return block


    def __s(self, block):
        res = 0

        for i in range(8):
            y = block & 0xf
            block >>= 4
            y = self._params.s_block[y]
            res |= y << (4 * i)

        return res


    def __p(self, block):
        res = 0

        for i in range(32):
            if block & 1:
                new_pos = (i * self._params.p_block_a + self._params.p_block_b) % 32
                res |= (1 << new_pos)

            block >>= 1

        return res
