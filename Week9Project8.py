def printAll(seq):
    if seq:
        print(seq[0])
        printAll(seq[1:])


printAll("Testing")
printAll((1, 2, 3, 4))
printAll([1, 2, 3, 4])