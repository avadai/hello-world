Python 3.8.4 (tags/v3.8.4:dfa645a, Jul 13 2020, 16:30:28) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def fib(n):
	if n < 3:
		return 1
	else:
		return fib(n - 1) + fib(n - 2)

	
>>> fib(6)
8
>>> 