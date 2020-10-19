Python 3.8.4 (tags/v3.8.4:dfa645a, Jul 13 2020, 16:30:28) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> f = open("myfile.txt", "w")
>>> f.write("First line.\nSecond line.\n")
25
>>> print()

>>> f.close()
>>> f = open("myfile.txt", "r")
>>> print(f.read())
First line.
Second line.

>>> f.close
<built-in method close of _io.TextIOWrapper object at 0x03554F28>
>>> f.close()
>>> 