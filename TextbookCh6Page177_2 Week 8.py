Python 3.8.4 (tags/v3.8.4:dfa645a, Jul 13 2020, 16:30:28) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def summation(lower, upper, margin):
	blanks = " " * margin
	print(blanks, lower, upper)
	if lower > upper:
		print(blanks, 0)
		return 0
	else:
		result = lower + summation(lower + 1, upper, margin +4)
		print(blanks, result)
		return result

	
>>> summation (1, 4, 0)
 1 4
     2 4
         3 4
             4 4
                 5 4
                 0
             4
         7
     9
 10
10
>>> 