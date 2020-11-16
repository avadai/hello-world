Python 3.8.4 (tags/v3.8.4:dfa645a, Jul 13 2020, 16:30:28) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from images import Image
>>> image = Image("smokey.gif")
>>> (r, g, b) = image.getPixel(0, 0)
>>> r
194
>>> g
221
>>> b
114
>>> image.setPixel(0, 0, (r + 10, g + 10, b + 10))
>>> def average(triple):
	(a, b, c) = triple
	return(a + b + c) // 3

>>> average((40, 50, 60))
50
>>> 