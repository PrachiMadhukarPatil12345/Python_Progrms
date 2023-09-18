Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print
<built-in function print>
>>> print(aditya)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print(aditya)
NameError: name 'aditya' is not defined
>>> print "hello"
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("hello")?
>>> print("hello")
hello
>>> print ("hare krishna hare krishna krishn ")
hare krishna hare krishna krishn 
>>> a=10
>>> print (a)
10
>>> a=30
>>> print (a)
30
>>> 20+60
80
>>> a=20
>>> b=20
>>> c=20
>>> print(a,b,c)
20 20 20
>>> a=b=c=d=50
>>> print(a)
50
>>> print(b)
50
>>> print(c)
50
>>> b,c,d=100
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    b,c,d=100
TypeError: cannot unpack non-iterable int object
>>> b,c,d=100,60,50
>>> print(b,c,d)
100 60 50
>>> 