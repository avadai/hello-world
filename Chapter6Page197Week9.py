Python 3.8.4 (tags/v3.8.4:dfa645a, Jul 13 2020, 16:30:28) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def odd(n): return n % 2 == 1

>>> list(filter(odd, range(10)))
[1, 3, 5, 7, 9]
>>> 