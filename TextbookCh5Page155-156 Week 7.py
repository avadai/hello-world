Python 3.8.4 (tags/v3.8.4:dfa645a, Jul 13 2020, 16:30:28) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> info = {}
>>> info["name"] = "Sandy"
>>> info["occupation"] = "hacker"
>>> info
{'name': 'Sandy', 'occupation': 'hacker'}
>>> info["occupation"] = "manager"
>>> info
{'name': 'Sandy', 'occupation': 'manager'}
>>> info["name"]
'Sandy'
>>> info["job"]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    info["job"]
KeyError: 'job'
>>> print(info.get("job", None))
None
>>> print(info.pop("job", None))
None
>>> print(info.pop("occupation"))
manager
>>> info
{'name': 'Sandy'}
>>> for key in info:
	print(key, info[key])

	
name Sandy
>>> grades = {90:'A', 80:'B', 70:'C'}
>>> list grades.items())
SyntaxError: invalid syntax
>>> list(grades.items())
[(90, 'A'), (80, 'B'), (70, 'C')]
>>> for (key, value) in grades.items():
	print(key, value)

	
90 A
80 B
70 C
>>> theKeys = list(info.keys())
>>> theKeys.sort()
>>> for key in theKeys:
	print(key, info[key])

	
name Sandy
>>> 