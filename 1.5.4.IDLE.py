Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a='since'
>>> b=1896
>>> print(a+repr(b))
since1896
>>> a+repr(b)
'since1896'
>>> #print出来是不带引号的
>>> 
>>> 
>>> 
>>> #转义符
>>> print("Hullo, I'm Felix.\My website is'www.gaoyaoxin.cn'")
Hullo, I'm Felix.\My website is'www.gaoyaoxin.cn'
>>> print("Hullo, I'm Felix.\    #直接在此换行
      
SyntaxError: EOL while scanning string literal
>>> #...(在行尾时) 续行符 可能是写到行尾时才加吧 不能手动换行，无论光标在一行中什么位置，都会直接开始运行了
>>> 
>>> 
>>> print("222222222222222222222222222222222222222222222222222222222222222222222222222")
222222222222222222222222222222222222222222222222222222222222222222222222222
>>> #看来会自动续行的，貌似上面的转义符没什么用了...
>>> 
>>> 
>>> print('Contact me via QQ\/Wechat\/Email)
      
SyntaxError: EOL while scanning string literal
>>> print('Contact me via QQ\/Wechat\/Email')
Contact me via QQ\/Wechat\/Email
>>> #后面的符号不能省略 会报错的| / 这个符号不需要转义符
>>> 
>>> print('QQ/Wechat')
QQ/Wechat
>>> print("QQ\Wechat")
QQ\Wechat
>>> # \ 看来也不需要借助转义符
>>> #1.5这节最后的例子貌似没什么用...
