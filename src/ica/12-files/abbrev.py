def print_abbrev(filename):
    file_in = open(filename, 'r')
    for line in file_in:
        line = line.strip()
        print(line[:20])
    file_in.close()

print_abbrev("../TextFiles/alice.txt")
