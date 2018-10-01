>>> l=[1,2,3,4]
>>> l
[1, 2, 3, 4]
>>> l.append
<built-in method append of list object at 0x7fccba63e188>
>>> l.append(5)
>>> 
>>> l
[1, 2, 3, 4, 5]
>>> l.append(10)
>>> l
[1, 2, 3, 4, 5, 10]
>>> a=['a','b','c']
>>> a
['a', 'b', 'c']
>>> a.index(a)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: ['a', 'b', 'c'] is not in list
>>> a.index('a')
0
>>> a.insert(3,'d')
>>> a
['a', 'b', 'c', 'd']
>>> a.remove('c')
>>> a
['a', 'b', 'd']
>>> 

