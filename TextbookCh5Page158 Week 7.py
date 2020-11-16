fileName = input("Enter the file name: ")
f = open(fileName, 'r')

words = []
for line in f:
    wordsInLine = line.split()
    for word in wordsInLine:
        words.append(word.upper())

theDictionary = {}
for word in words:
    number = theDictionary.get(word, None)
    if number is None:
        theDictionary[word] = 1
    else:
        theDictionary[word] = number + 1

theMaximum = max(theDictionary.values())
for key in theDictionary:
    if theDictionary[key] == theMaximum:
        print("The mode is", key)
        break

