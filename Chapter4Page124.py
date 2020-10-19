Python 3.8.4 (tags/v3.8.4:dfa645a, Jul 13 2020, 16:30:28) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import os
>>> currentDirectoryPath = os.getcwd()
>>> listOfFileNames = os.listdir(currentDirectoryPath)
>>> for name in listOfFileNames:
	if ".py" in name:
		print(name)

		
test.py
Week4Page69.py
>>> 