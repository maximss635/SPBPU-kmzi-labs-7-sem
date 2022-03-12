import pytest

from sp_network import *
from crypt_model import *


class TestSpNetwork:
    def test_s_block(self):
        model = SPNetwork(Params())

        assert(0xeeeeeeee == model._SPNetwork__s(0))
        assert(0xeeeeeee3 == model._SPNetwork__s(1))
        assert(0xeeeeeeed == model._SPNetwork__s(2))
        assert(0xeeeeeee2 == model._SPNetwork__s(3))

        assert(0xeeeeeed0 == model._SPNetwork__s(0x25))

        assert(0x33dd2277 == model._SPNetwork__s(0x11223344))
        assert(0xeeee3d27 == model._SPNetwork__s(0x1234))
        assert(0x6ac47b82 == model._SPNetwork__s(0x6fac48e3))


    def test_p_block(self):
        model = SPNetwork(Params())

        assert(0x00000020 == model._SPNetwork__p(1))
        assert(0x04000000 == model._SPNetwork__p(2))
        assert(0x04000020 == model._SPNetwork__p(3))
        assert(0x00008000 == model._SPNetwork__p(4))


class TestCryptModel:
    def test_danya(self):
        model = CryptModel(ParamsDanyas(), 'OFB')

        iv  = 0x03ea138e
        key = 0x0153f9a8
        file_in = '../Даня/In/test2.in'
        file_out = '../Даня/Out/my_test2.out'

        model.exec(file_in, file_out, key, iv)


    def test_danya_examples(self):
        model = CryptModel(ParamsDanyas())

        key = 0x4d4b20d8

        file_in_1 = '../Даня/In/example1.in'
        file_in_2 = '../Даня/In/example2.in'
        file_in_3 = '../Даня/In/example3.in'
        file_out_1 = '../Даня/Out/my_example1.out'
        file_out_2 = '../Даня/Out/my_example2.out'
        file_out_3 = '../Даня/Out/my_example3.out'

        model.exec(file_in_1, file_out_1, key)
        model.exec(file_in_2, file_out_2, key)
        model.exec(file_in_3, file_out_3, key)


if __name__ == "__main__":
    pytest.main()
