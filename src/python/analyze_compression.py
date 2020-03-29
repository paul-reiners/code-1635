if __name__ == "__main__":
    file1 = open('/Users/reiners/Dropbox/projects/code-1635/out/1635_16.txt', 'r')
    count = 0

    while True:
        count += 1

        line = file1.readline()

        if not line:
            break
        print("Line{}: {}".format(count, line.strip()))

    file1.close()
