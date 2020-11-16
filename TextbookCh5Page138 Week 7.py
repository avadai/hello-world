Python 3.8.4 (tags/v3.8.4:dfa645a, Jul 13 2020, 16:30:28) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> example = [1, 2, 3, 4]
>>> example
[1, 2, 3, 4]
>>> example[3] = 0
>>> example
[1, 2, 3, 0]
>>> number = [2, 3, 4, 5]
>>> number
[2, 3, 4, 5]
>>> for index in range(len(number)):
	number[index] = number[index] ** 2

	
>>> number
[4, 9, 16, 25]
>>> sentence = "This example has five word."
>>> words = sentence.split()
>>> words
['This', 'example', 'has', 'five', 'word.']
>>> for index in range(len(words)):
	words[index] = words[index].upper()

	
>>> words
['THIS', 'EXAMPLE', 'HAS', 'FIVE', 'WORD.']
>>> 