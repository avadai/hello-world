Python 3.8.4 (tags/v3.8.4:dfa645a, Jul 13 2020, 16:30:28) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> help(round)
Help on built-in function round in module builtins:

round(number, ndigits=None)
    Round a number to a given precision in decimal digits.
    
    The return value is an integer if ndigits is omitted or None.  Otherwise
    the return value has the same type as the number.  ndigits may be negative.

>>> import math
>>> dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
>>> math.pi
3.141592653589793
>>> math.sqrt(2)
1.4142135623730951
>>> help(math.cos)
Help on built-in function cos in module math:

cos(x, /)
    Return the cosine of x (measured in radians).

>>> from math import pi, sqrt
>>> print(pi, sqrt(2))
3.141592653589793 1.4142135623730951
>>> import taxform
Enter the gross income: 120000
Enter the number of dependents: 2
The income tax is $20800.0
>>> help(taxform)
Help on module taxform:

NAME
    taxform

DESCRIPTION
    Program: taxform.py
    Author: Ken Lambert
    
    Compute a person's income tax.
    
    1. Significant constants
           tax rate
           standard deduction
           deduction per dependent
    2. The inputs are
           gross income 
           number of dependents 
    3. Computations:
           taxable income = gross income - the standard deduction - 
                            a deduction for each dependent 
           income tax = is a fixed percentage of the taxable income 
    4. The outputs are
           the income tax

DATA
    DEPENDENT_DEDUCTION = 3000.0
    STANDARD_DEDUCTION = 10000.0
    TAX_RATE = 0.2
    grossIncome = 120000.0
    incomeTax = 20800.0
    numDependents = 2
    taxableIncome = 104000.0

FILE
    c:\users\awvad\onedrive\desktop\homework-laptop-mb9soode-laptop-mb9soode\script programming\taxform.py


>>> 