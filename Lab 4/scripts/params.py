def left_cycle_shift(a, n):
    assert(n > 0)
    return (a << n) & 0xffff | a >> (16 - n)


def concat_words(a, b):
    return (a << 16) | b


class ParamsDanyas:
    def __init__(self):
        self.s_block = [5, 6, 12, 3, 1, 0, 13, 4, 15, 10, 2, 11, 9, 7, 14, 8]
        self.p_block_a, self.p_block_b = 5, 20


class Params:
    def __init__(self):
        self.s_block = [14, 3, 13, 2, 7, 0, 6, 9, 11, 15, 12, 1, 4, 5, 8, 10]
        self.p_block_a, self.p_block_b = 21, 5
