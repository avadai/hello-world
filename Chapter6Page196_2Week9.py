Python 3.8.4 (tags/v3.8.4:dfa645a, Jul 13 2020, 16:30:28) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> words = ["231", "20", "-45", "99"]
>>> map(int, words)
<map object at 0x038469B8>
>>> words
['231', '20', '-45', '99']
>>> words = list(map(int, words))
>>> words
[231, 20, -45, 99]
>>> 