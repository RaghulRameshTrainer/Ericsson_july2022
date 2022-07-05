Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> math.sqrt(100)
10.0
>>> math.factorial(5)
120
>>> math.factorial(10)
3628800
>>> math.factorial(100)
93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
>>> math.prod(10,20)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    math.prod(10,20)
TypeError: prod() takes exactly 1 positional argument (2 given)
>>> math.prod([10,20])
200
>>> math.ceil(77.7)
78
>>> math.floor(77.7)
77
>>> round(434.3)
434
>>> math.log10(1000)
3.0
>>> math.log2(256)
8.0
>>> math.log(43,7)
1.9328745047758362
>>> math.log(49,7)
2.0
>>> math.sin(0)
0.0
>>> math.cos(0)
1.0
>>> math.tan(0)
0.0
>>> math.tan(60)
0.320040389379563
>>> math.sin(60)
-0.3048106211022167
>>> math.pi
3.141592653589793
>>> math.e
2.718281828459045
>>> print(dir(math))
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
>>> math.exp(2,4)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    math.exp(2,4)
TypeError: exp() takes exactly one argument (2 given)
>>> math.exp([2,4])
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    math.exp([2,4])
TypeError: must be real number, not list
>>> math.exp(5)
148.4131591025766
>>> math.isqrt(100)
10
>>> #datetime and logging