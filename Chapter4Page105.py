Python 3.8.4 (tags/v3.8.4:dfa645a, Jul 13 2020, 16:30:28) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name = "myfile.txt"
>>> name[0:]
'myfile.txt'
>>> name[0:1]
'm'
>>> name[0:2]
'my'
>>> name[:len(name)]
'myfile.txt'
>>> name[-3:]
'txt'
>>> name[2:6]
'file'
>>> 