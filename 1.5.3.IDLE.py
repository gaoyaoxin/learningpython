Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a='1896'
>>> type(a)
<class 'str'>
>>> a=int(a)
>>> type(a)
<class 'int'>
>>> class(a)
SyntaxError: invalid syntax
>>> #虽然下面显示的是class 但还是只能用type()看对象类型
>>> b=1999
>>> type(b)
<class 'int'>
>>> b=str(b)
>>> type(b)
<class 'str'>
>>> b
'1999'
>>> #整数和字符串可以互换
>>> c=5.20
>>> type(c)
<class 'float'>
>>> c=str(c)
>>> type(c)
<class 'str'>
>>> c
'5.2'
>>> d='5.20'
>>> type(c)
<class 'str'>
>>> d=float(d)
>>> type(d)
<class 'float'>
>>> d
5.2
>>> ```
SyntaxError: invalid syntax
>>> ```浮点数和字符串也可以互换
SyntaxError: invalid syntax
>>> #不过把小数点以后的零舍掉了
>>> love='5.20'
>>> love
'5.20'
>>> #而字符串里的东西是不会被舍掉的
>>> 
>>> 
>>> 
>>> 
>>> 
>>> e=6.78
>>> e=int(e)
>>> e
6
>>> type(e)
<class 'int'>
>>> #浮点数可以转换为整数，即取整
>>> f=-5.93
>>> f=int(f)
>>> f
-5
>>> #看来不是取整，而只是将小数部分直接拿掉
>>> #更精确地说，正数是向下取整，而负数是向上取整
>>> 
>>> 
>>> 
>>> 
>>> g=5
>>> g=float(g)
>>> g
5.0
>>> 整数转换为浮点数自动取了小数点后一位的精确度
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    整数转换为浮点数自动取了小数点后一位的精确度
NameError: name '整数转换为浮点数自动取了小数点后一位的精确度' is not defined
>>> 



>>> 
>>> 
>>> 
>>> 
>>> #TODO 思考如何在python里取整（向下取整）、如何向上取整
