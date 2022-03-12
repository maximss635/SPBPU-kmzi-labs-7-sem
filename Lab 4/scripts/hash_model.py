from sp_network import *
import os


class HashModel(SPNetwork):
    def __init__(self, params):
        super().__init__(params)


    def exec(self, file_path, y0):
        assert(isinstance(y0, int))

        file_size = os.path.getsize(file_path)
        print('File size = {}'.format(file_size))

        additional_block = file_size
        print('Additional block = {}'.format(hex(additional_block)))

        n_blocks = file_size // 4
        last_block_size = file_size % 4

        if last_block_size == 0:
            last_block_size = 4
        else:
            n_blocks += 1

        print('N blocks = {}'.format(n_blocks))
        print('last block size = {}'.format(last_block_size))

        file = open(file_path, 'rb')

        #print('\ty = {}'.format(hex(y0)))
        y = self.__step_hash_function(additional_block, y0)
        #print('\ty = {}'.format(hex(y)))

        # Read block by block
        for i in range(n_blocks):
            if i != n_blocks - 1:
                block = file.read(4)
                block = bytes_to_integer(block, 4)
            else:
                block = file.read(last_block_size)
                block = bytes_to_integer(block, last_block_size)

                print('last block = {}'.format(hex(block)))
                if last_block_size == 3:
                    block <<= 8
                    block |= 0b11111111
                elif last_block_size == 2:
                    block <<= 16
                    block |= 0b1111111111111111
                elif last_block_size == 1:
                    block <<= 24
                    block |= 0b111111111111111111111111

                print('last block = {}'.format(hex(block)))

            y = self.__step_hash_function(block, y)
            #print('\ty = {}'.format(hex(y)))

        file.close()

        return y


    def __step_hash_function(self, x, y):
        # F{X+Y}(X+Y) + X + Y
        return self.convert_block(x ^ y, x ^ y) ^ x ^ y
