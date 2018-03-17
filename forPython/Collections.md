
Collections模块是在内置数据类型（dict、list、set、tuple）的基础上，提供了一些额外的数据类型，常用的有：OrderedDict、defaultdict、nametuple、deque、Counter等

### 1.Counter
Counter是一个计数器，它实际上是dict的一个子类，也就是它的元素也是无序的


```python
from collections import Counter

str_1 = 'dfafaabbccfcd'
c_str = Counter(str_1)
c_str
```




    Counter({'a': 3, 'b': 2, 'c': 3, 'd': 2, 'f': 3})




```python
c_str.most_common(3)  # most_common(n) 返回数量排前n的元素以及数量
```




    [('f', 3), ('a', 3), ('c', 3)]




```python
list(c_str.elements())  # .elements() 返回所有元素并且按str_1下标排序
```




    ['d', 'd', 'f', 'f', 'f', 'a', 'a', 'a', 'b', 'b', 'c', 'c', 'c']



利用Counter进行运算，&表示取两个数目中最小的一个(如果只存在一个集合中，则结果集不会存在该元素)，|表示取数目中最大的一个


```python
print(c_str)
c_str & Counter({'a':1, 'b':1, 'c':1})
```

    Counter({'f': 3, 'a': 3, 'c': 3, 'd': 2, 'b': 2})





    Counter({'a': 1, 'b': 1, 'c': 1})




```python
c_str | Counter(a=5, f=20)  # Counter初始化方式跟字典一样，有多种方式
```




    Counter({'a': 5, 'b': 2, 'c': 3, 'd': 2, 'f': 20})




```python
c_str + Counter({'a':1, 'b':1, 'c':1})
```




    Counter({'a': 4, 'b': 3, 'c': 4, 'd': 2, 'f': 3})




```python
c_str - Counter({'a':10, 'b':1, 'c':1})  # 进行运算操作时，如果数目结果为负的会被直接忽略
```




    Counter({'b': 1, 'c': 2, 'd': 2, 'f': 3})



可以看出Counter除了统计数量，对字典之间做运算也是非常方便的。

### 2. defaultdict


```python
from collections import defaultdict

num = defaultdict(0)  
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-19-3e7a84671f0c> in <module>()
          1 from collections import defaultdict
          2 
    ----> 3 num = defaultdict(0)
    

    TypeError: first argument must be callable or None



```python
num = defaultdict(lambda: 0)
for index, i in enumerate('abcdef'):
    num[i] += index
num
```




    defaultdict(<function __main__.<lambda>>,
                {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5})




```python
lst = defaultdict(list)
for index, i in enumerate('abcdef'):
    lst[i].append(index)
lst
```




    defaultdict(list, {'a': [0], 'b': [1], 'c': [2], 'd': [3], 'e': [4], 'f': [5]})



### 3. deque
deque是一个双端队列，与list类似，但list不支持左边增删元素，而deque提供了appendleft()和popleft()的支持


```python
from collections import deque

dq = deque(maxlen=5)  # 只保留5个元素
dq.extend(range(10))
dq
```




    deque([5, 6, 7, 8, 9])



使用rotate方法让元素前移或后移


```python
dq = deque('abcdef')
print(dq)

dq.rotate(2)  # 所有元素向前移动2个位置
print(dq)

dq.rotate(-2) # 所有元素向后移动2个位置
print(dq)
```

    deque(['a', 'b', 'c', 'd', 'e', 'f'])
    deque(['e', 'f', 'a', 'b', 'c', 'd'])
    deque(['a', 'b', 'c', 'd', 'e', 'f'])


### 4. nametuple

namedtuple继承于tuple，最大特点是给元组每个位置的元素设置了别名，增加程序的可读性，而且namedtuple是可修改的


```python
from collections import namedtuple

Point = namedtuple('point', ['x', 'y'])
p = Point(10, y=20)
p
```




    point(x=10, y=20)




```python
print(p.x+p.y)

print(p[0]+p[1])  # 类似普通元组一样通过下标访问元素

x, y = p  # 元组拆分
print(x+y)
```

    30
    30
    30



```python
print(p._replace(x=20))  # 修改元素的值
print(p._asdict())   # 转换成字典（有序字典）
```

    point(x=20, y=20)
    OrderedDict([('x', 10), ('y', 20)])


### 5. OrderedDict
OrderedDict继承与dict, 元素有序存储，顺序为按元素插入时的顺序


```python
from collections import OrderedDict

dic = OrderedDict()
dic['k1'] = 'v1'
dic['k2'] = 'v2'
dic['k3'] = 'v3'
print(dic)
```

    OrderedDict([('k1', 'v1'), ('k2', 'v2'), ('k3', 'v3')])



```python
# 按元素插入的顺序排序，一般用于字典排序
d = {v: i for i, v in enumerate('abcdefg')}
od = OrderedDict(sorted(d.items(), key=lambda x:x[1]))  # 无序字典d排序后，转换成有序字典
od  # 遍历方式一样  for k, v in od.items()
```




    OrderedDict([('a', 0),
                 ('b', 1),
                 ('c', 2),
                 ('d', 3),
                 ('e', 4),
                 ('f', 5),
                 ('g', 6)])


