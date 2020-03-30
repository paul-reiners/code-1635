import sys

from zlib import compress


def main(in_file_path, out_file_path):
    in_file = open(in_file_path, 'r')
    out_file = open(out_file_path, "w")
    out_file.write("generation,width,compressed-width,compression-ratio\n")
    count = 0

    while True:
        line = in_file.readline().strip()
        bs = bytes(line, encoding='utf8')
        orig_size = len(bs)
        if orig_size == 0:
            break
        compressed_size = len(compress(bs))
        ratio = float(compressed_size) / float(orig_size)

        if not line:
            break
        print("{}, {}, {}, {}".format(count, orig_size, compressed_size, ratio))
        out_file.write("{},{},{},{}".format(count, orig_size, compressed_size, ratio))
        out_file.write("\n")
        count += 1

    in_file.close()
    out_file.close()


if __name__ == "__main__":
    rule = 1635
    n = sys.argv[1]
    input_file_path = "out/{}_{}.txt".format(rule, n)
    output_file_path = "out/{}_{}_compression.txt".format(rule, n)
    main(input_file_path, output_file_path)
