Python 3.8.4 (tags/v3.8.4:dfa645a, Jul 13 2020, 16:30:28) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> f = open("integers.txt", 'w')
>>> for count in range(500):
	number = random.randint(1, 500)
	f.write(str(number) + '\n')

	
4
4
4
4
4
2
4
4
4
4
4
4
4
4
4
4
4
4
4
2
4
4
3
2
4
3
4
4
3
4
3
4
4
4
4
4
4
4
4
4
4
4
3
2
4
4
4
4
4
4
3
3
4
3
4
4
4
4
4
3
4
4
4
4
3
4
4
4
4
4
4
4
4
3
3
4
4
3
4
4
4
4
4
4
4
4
4
3
4
4
4
4
4
4
4
4
4
4
4
4
3
3
4
4
3
4
4
4
4
3
4
4
4
4
4
4
4
4
4
4
4
4
3
4
4
4
4
4
4
3
4
4
4
4
3
4
4
4
4
4
2
3
4
4
4
4
4
4
4
4
3
4
4
3
3
4
4
4
4
4
3
4
4
3
3
4
4
4
4
4
4
3
4
4
4
4
2
4
4
4
4
4
4
4
4
4
4
4
3
3
4
4
4
3
4
4
4
4
4
4
4
4
4
4
3
4
4
4
4
4
4
4
3
4
3
3
4
4
4
4
4
3
4
4
4
4
4
4
4
4
4
4
4
4
4
3
4
4
4
3
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
3
4
4
4
4
4
4
4
4
4
4
4
3
3
3
4
4
3
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
3
4
4
4
4
4
4
4
3
4
4
4
4
4
3
4
4
4
4
4
3
4
4
4
3
4
4
3
3
4
4
4
4
3
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
4
3
4
4
4
4
4
3
4
4
4
4
4
4
4
4
4
4
3
4
3
4
4
4
4
4
3
4
4
4
3
4
4
3
4
4
3
4
4
4
4
3
4
4
4
4
4
4
4
4
3
4
4
3
4
2
4
4
3
4
4
4
4
3
4
4
4
4
3
4
4
3
4
3
4
4
4
4
4
4
4
4
4
4
4
3
4
4
3
3
4
4
3
4
4
3
4
4
4
4
4
3
3
4
3
4
3
4
4
4
4
4
3
3
4
3
4
4
4
4
2
4
3
4
3
3
4
4
3
4
4
4
4
3
4
4
4
4
4
4
3
4
4
4
4
4
4
4
4
3
4
4
4
4
4
4
2
>>> f.close()
>>> f = open("integer.txt", 'r')
>>> print(f.read())

>>> 