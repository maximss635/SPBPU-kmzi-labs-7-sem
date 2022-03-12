def left_cycle_shift(a, n):
    assert(n > 0)
    return (a << n) & 0xffff | a >> (16 - n)


def concat_words(a, b):
    return (a << 16) | b


class Params:
    def __init__(self):
        self.s_block = [14, 3, 13, 2, 7, 0, 6, 9, 11, 15, 12, 1, 4, 5, 8, 10]
        self.p_block_a, self.p_block_b = 21, 5
