from hash_model import *
from sys import argv


def main():
    if len(argv) != 4:
        print('Usage:\n\tpython main.py <path_in_file> <path_H0> <path_out_file>')
        exit(0)

    path_in_file = argv[1]

    f = open(argv[2], 'rb')
    h0 = bytes_to_integer(f.read(4), 4)
    f.close()

    print('h0 = {}'.format(hex(h0)))

    model = HashModel(Params())
    hash = model.exec(path_in_file, h0)

    print('Hash = {}'.format(hex(hash)))

    f = open(argv[3], 'wb')
    f.write(hash.to_bytes(4, byteorder='big'))



if __name__ == "__main__":
    main()
