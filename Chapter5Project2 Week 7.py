import linecache
file = input("Enter a filename: ")
f = open(file, 'r')
numLines = len(open(file).readlines( ))
print("The file has", numLines, "lines.")

while numLines > 0:
    x = int(input("What line would you like to see? "))
    all_lines = open(file).readlines()
    print(linecache.getline(file, x))
    if x <= 0 or x > numLines:
        break