Python 3.8.4 (tags/v3.8.4:dfa645a, Jul 13 2020, 16:30:28) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def summation(lower, upper):
	if lower > upper:
		return 0
	else:
		return lower + summation (lower + 1, upper)

	
>>> summation(1,5)
15
>>> 