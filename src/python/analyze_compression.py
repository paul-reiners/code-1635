import sys

from zlib import compress


def main(in_file_path, out_file_path):
    in_file = open(in_file_path, 'r')
    out_file = open(out_file_path, "w")
    out_file.write("row,width,compressed-width,compression-ratio\n")
    count = 0

    while True:
        line = in_file.readline().strip()
        orig_size = len(line)
        if orig_size == 0:
            break
        compressed_size = len(compress(line))
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
    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    main(input_file_path, output_file_path)
