import sys

from zlib import compress

if __name__ == "__main__":
    file_path = sys.argv[1]
    file1 = open(file_path, 'r')
    count = 0

    while True:
        count += 1

        line = file1.readline().strip()
        orig_size = len(line)
        if orig_size == 0:
            continue
        compressed_size = len(compress(line))
        ratio = float(compressed_size) / float(orig_size)

        if not line:
            break
        print("{}, {}, {}".format(orig_size, compressed_size, ratio))

    file1.close()
