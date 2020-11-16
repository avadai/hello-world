Python 3.8.4 (tags/v3.8.4:dfa645a, Jul 13 2020, 16:30:28) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def example(required, option1 = 2, option2 = 3):
	print(required, option1, option2)

	
>>> example(1)
1 2 3
>>> example(1, 10)
1 10 3
>>> example(1, 10, 20)
1 10 20
>>> example(1, option2 = 20)
1 2 20
>>> example(1, option2 = 20, option1 = 10)
1 10 20
>>> 