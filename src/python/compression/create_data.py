import sys

from zlib import compress


def create_data(generation_count, only_measure_within_light_come=True):
    rule = 1635
    in_file_path = "out/ca/{}_{:05d}.txt".format(rule, generation_count)
    out_file_path = "out/compression/{}_{:05d}_compression.txt".format(rule, generation_count)
    in_file = open(in_file_path, 'r')
    out_file = open(out_file_path, "w")
    out_file.write("generation,width,compressed-width,compression-ratio\n")

    count = 0
    first_line = peek_line(in_file)
    width = len(first_line)
    center = (width - 1) // 2

    while True:
        line = in_file.readline().strip()
        if only_measure_within_light_come:
            segment_to_measure = line[center - count:center + count + 1]
        else:
            segment_to_measure = line
        line_bytes = bytes(segment_to_measure, encoding='utf8')
        orig_size = len(line_bytes)
        if orig_size == 0:
            break
        compressed_size = len(compress(line_bytes))
        ratio = float(compressed_size) / float(orig_size)

        if not line:
            break
        print("{}, {}, {}, {}".format(count, orig_size, compressed_size, ratio))
        out_file.write("{},{},{},{}".format(count, orig_size, compressed_size, ratio))
        out_file.write("\n")
        count += 1

    in_file.close()
    out_file.close()


def peek_line(f):
    pos = f.tell()
    line = f.readline().strip()
    f.seek(pos)
    return line


if __name__ == "__main__":
    n = int(sys.argv[1])
    create_data(n)
