from sp_network import *

import os


class CryptModel(SPNetwork):
    def __init__(self, params, mode=None):
        super().__init__(params)
        self.__mode = mode


    def exec(self, file_in_path, file_out_path, key, y0=None):
        assert(isinstance(key, int))

        file_size = os.path.getsize(file_in_path)
        n_blocks = file_size // 4
        last_block_size = file_size % 4
        if last_block_size == 0:
            last_block_size = 4
        else:
            n_blocks += 1

        file_in = open(file_in_path, 'rb')
        file_out = open(file_out_path, 'wb')

        converted_block = y0
        gamma = y0
        cnt = y0

        # Read block by block
        for i in range(n_blocks):
            if i != n_blocks - 1:
                block = file_in.read(4)
                block = bytes_to_integer(block, 4)
            else:
                # Last block
                block = file_in.read(last_block_size)
                block = bytes_to_integer(block, last_block_size)

            if self.__mode is None:
                converted_block = self.convert_block(block, key)
            elif self.__mode == 'CBC':
                converted_block = self.convert_block(block ^ converted_block, key)
            elif self.__mode == 'CFB':
                converted_block = self.convert_block(block, key) ^ converted_block
            elif self.__mode == 'OFB':
                gamma = self.convert_block(gamma, key)
                converted_block = block ^ gamma
            elif self.__mode == 'CTR':
                converted_block = block ^ gamma
                gamma = self.convert_block(cnt, key)
                cnt = (self._params.cnt_a * cnt + self._params.cnt_b) % (2 ** 32)

            file_out.write(converted_block.to_bytes(4, byteorder='big'))

        file_in.close()
        file_out.close()
