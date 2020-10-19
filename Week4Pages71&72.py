Python 3.8.4 (tags/v3.8.4:dfa645a, Jul 13 2020, 16:30:28) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for exponent in range(7, 11):
	print(exponent, 10 ** exponent)

	
7 10000000
8 100000000
9 1000000000
10 10000000000
>>> "%6s" % "four"
'  four'
>>> "%-6s" % "four"
'four  '
>>> for exponent in range(7, 11):
	print("%-3d%12d" % (exponent, 10 ** exponent))

	
7      10000000
8     100000000
9    1000000000
10  10000000000
>>> salary = 100.00
>>> print("Your salary is $" + str(salary))
Your salary is $100.0
>>> print("Your salary is $%0.2f" % salary)
Your salary is $100.00
>>> "%6.3f" % 3.14
' 3.140'
>>> 