import sys


def hamming_distance(s1, s2):
    dist = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            dist += 1

    return dist


def create_data(generation_count):
    rule = 1635
    in_file_path = "out/ca/{}_{}.txt".format(rule, generation_count)
    out_file_path = "out/hamming-distance/{}_{}_hamming-distance.txt".format(rule, generation_count)
    in_file = open(in_file_path, 'r')
    out_file = open(out_file_path, "w")
    out_file.write("generation,hamming-distance-from-prev-gen\n")
    count = 0

    prev_line = in_file.readline().strip()
    width = len(prev_line)
    mid_point = (width - 1) // 2
    while True:
        cur_line = in_file.readline().strip()
        if not cur_line or len(cur_line) == 0:
            break

        # Each generation on RHS moves to right one cell.
        prev_gen_growth = prev_line[mid_point:mid_point + count + 1]
        cur_gen_growth = cur_line[mid_point + 1: mid_point + count + 2]
        d = hamming_distance(prev_gen_growth, cur_gen_growth)

        print("{}, {}".format(count, d))
        out_file.write("{},{}".format(count, d))
        out_file.write("\n")

        prev_line = cur_line
        count += 1

    in_file.close()
    out_file.close()


if __name__ == "__main__":
    n = sys.argv[1]
    create_data(n)
