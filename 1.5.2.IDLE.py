Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a='since'
>>> b=1896
>>> print `a`+b
SyntaxError: Missing parentheses in call to 'print'
>>> #python3已经弃用使用此方法拼接两个对象
>>> print str(a)+b
SyntaxError: invalid syntax
>>> str(a)
'since'
>>> print str(a) + b
SyntaxError: invalid syntax
>>> print(str(a)+b)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print(str(a)+b)
TypeError: Can't convert 'int' object to str implicitly
>>> print (a+str(b))
since1896
>>> #囧！应该将整数转换为字符串
