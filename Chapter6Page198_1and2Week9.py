Python 3.8.4 (tags/v3.8.4:dfa645a, Jul 13 2020, 16:30:28) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from functools import reduce
>>> def add(x, y): return x + y

>>> def multiply(x, y): return x *y

>>> data = [1, 2, 3, 4]
>>> reduce(add, data)
10
>>> reduce(multiply, data)
24
>>> data = [1, 2, 3, 4]
>>> reduce(lambda x, y: x + y, data)
10
>>> reduce(lambda x, y: x * y, data)
24
>>> 