Python 3.8.4 (tags/v3.8.4:dfa645a, Jul 13 2020, 16:30:28) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def repToInt(repString, base = 2):
	decimal = 0
	exponent = len(repString) - 1
	for digit in repString:
		decimal = decimal + int(digit) * base ** exponent
		exponent -= 1
	return decimal

>>> repToInt("10", 10)
10
>>> repToInt("10", 8)
8
>>> repToInt("10", 2)
2
>>> repToInt("10")
2
>>> 