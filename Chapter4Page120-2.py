Python 3.8.4 (tags/v3.8.4:dfa645a, Jul 13 2020, 16:30:28) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> f = open("myfile.txt", 'r')
>>> text = f.read()
>>> text
'First line.\nSecond line.\n'
>>> print(text)
First line.
Second line.

>>> f = open("myfile.txt", 'r')
>>> for line in f:
	print(line)

	
First line.

Second line.

>>> 