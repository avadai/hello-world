iFile = input("Enter the input file name: ")
OFile = input("Enter the output file name: ")

with open(iFile, 'r') as f, open(OFile, 'w') as w:
    num = 0
    for line in f:
        num += 1
        w.write('{:>4}> {}'.format(num, line))