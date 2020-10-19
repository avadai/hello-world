Python 3.8.4 (tags/v3.8.4:dfa645a, Jul 13 2020, 16:30:28) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name = "Alan Turing"
>>> name[0]
'A'
>>> name[3]
'n'
>>> name[len(name)]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    name[len(name)]
IndexError: string index out of range
>>> name[len(name) - 1]
'g'
>>> name[-1]
'g'
>>> name[-2]
'n'
>>> 