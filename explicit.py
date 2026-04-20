Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=10
>>> print(a)
10
>>> print(type(a))
<class 'int'>
>>> b=23.5
>>> print(type(b))
<class 'float'>
>>> num1=10
>>> num2=4.4
>>> sum=num1+num2
>>> print("the sum of:",sum)
the sum of: 14.4
>>> print(type(sum))
<class 'float'>
>>> numstr='12'
>>> print(numstr)
12
>>> numstr=12
>>> num1=14
>>> print(type(numsrt))
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print(type(numsrt))
NameError: name 'numsrt' is not defined. Did you mean: 'numstr'?
>>> numstr=12
>>> num1=14
>>> print(type(numstr))
<class 'int'>
>>> numstr='12'
>>> num1=14
>>> print(type(numstr))
<class 'str'>
>>> numstr=int(numstr)
>>> numbsum=numstr*numstr
>>> print(numbsum)
144
>>> print(type(numstr))
<class 'int'>
