Python 3.8.4 (tags/v3.8.4:dfa645a, Jul 13 2020, 16:30:28) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def summation(lower, upper):
	result = 0
	while lower <= upper:
		result += lower
		lower += 1
	return result

>>> summation(1,4)
10
>>> summation(50,100)
3825
>>> 