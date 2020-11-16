Python 3.8.4 (tags/v3.8.4:dfa645a, Jul 13 2020, 16:30:28) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> abs
<built-in function abs>
>>> import math
>>> math.sqrt
<built-in function sqrt>
>>> f = abs
>>> f
<built-in function abs>
>>> f(-4)
4
>>> funcs = [abs, math.sqrt]
>>> funcs
[<built-in function abs>, <built-in function sqrt>]
>>> funcs[1](2)
1.4142135623730951
>>> 