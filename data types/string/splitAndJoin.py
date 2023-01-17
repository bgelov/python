def split_and_join(line):
    LineSplit = line.split(" ")
    LineJoin = "-".join(LineSplit)
    return LineJoin

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
