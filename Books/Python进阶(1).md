
#### 1. deque 只保留有限的几个元素的历史记录


```python
from collections import deque

dq = deque(maxlen=5)
for i in range(1, 20):
    dq.append(i)
    
print(dq)
```

    deque([15, 16, 17, 18, 19], maxlen=5)


#### 2.  headq 从集合中获取最大或最小的n个元素  (n=1的时候直接用max、min)


```python
import heapq
lst = [7, 2, 3, 4, 9, 1]
print(heapq.nlargest(3, lst))  # 按大到小排序
print(heapq.nsmallest(3, lst))  # 按小到大排序
```

    [9, 7, 4]
    [1, 2, 3]



```python
# Transform list into a heap 堆数据结构重要特征是heap[0]元素永远是最小的
heapq.heapify(lst)
lst
# 还可以使用key，对字典、元组排序
dct = [('A', 10), ('B', 5), ('C', 4), ('D', 18)]
print(heapq.nsmallest(3, dct, key=lambda x: x[1]))
```

    [('C', 4), ('B', 5), ('A', 10)]



```python
from operator import itemgetter

# 更高级点的列子
portfolio = [
	{'name': 'IBM', 'shares': 100, 'price': 91.1}, 
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
	{'name': 'FB', 'shares': 200, 'price': 21.09}, 
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
	{'name': 'YHOO', 'shares': 45, 'price': 16.35}, 
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
print(heapq.nlargest(2, portfolio, key=lambda x: x['price']))  # 最贵的2个
print(heapq.nlargest(2, portfolio, key=itemgetter('price', 'name')))  # 不用lambda并且按多个排序
print(heapq.nlargest(2, portfolio, key=lambda x: (x['price'], x['name']))) # 最贵的2个
```

    [{'name': 'AAPL', 'shares': 50, 'price': 543.22}, {'name': 'ACME', 'shares': 75, 'price': 115.65}]
    [{'name': 'AAPL', 'shares': 50, 'price': 543.22}, {'name': 'ACME', 'shares': 75, 'price': 115.65}]
    [{'name': 'AAPL', 'shares': 50, 'price': 543.22}, {'name': 'ACME', 'shares': 75, 'price': 115.65}]


#### 3. 字典的一些相关知识


```python
prices = {
    'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75
}
# 字典反转
print(dict(zip(prices.values(), prices.keys())))  # 方法一
print({v: k for k, v in prices.items()})  # 方法二

# 你可能不知道：一个 OrderedDict 的大小是一个普通字典的两倍，因为它内部维 护着另外一个链表
```

    {45.23: 'ACME', 612.78: 'AAPL', 205.55: 'IBM', 37.2: 'HPQ', 10.75: 'FB'}
    {45.23: 'ACME', 612.78: 'AAPL', 205.55: 'IBM', 37.2: 'HPQ', 10.75: 'FB'}



```python
print(min(zip(prices.values(), prices.keys())))  # 排序
print(min(prices.items()))  # 默认一些数学运算都会作用于第一个元素
print(sorted(zip(prices.values(), prices.keys())))  # 排序
```

    (10.75, 'FB')
    ('AAPL', 612.78)
    [(10.75, 'FB'), (37.2, 'HPQ'), (45.23, 'ACME'), (205.55, 'IBM'), (612.78, 'AAPL')]



```python
# 字典合并
dct = {'A': 1, 'B': 2}
# print(dict(prices.items() + dct.items()))  # Python2.7支持
print(dict(list(prices.items()) + list(dct.items())))  # python3

dct.update(prices) # 方法2
print(dct)
```

    {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.2, 'FB': 10.75, 'A': 1, 'B': 2}
    {'A': 1, 'B': 2, 'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.2, 'FB': 10.75}


#### 4. 列表的列表如何快速去重？


```python
lst = [[1, 2], [1, 2], [2, 3]]
lst2 = map(tuple, lst)  # 列表无法直接set，转元组后进行set去重
print(set(lst2))
```

    {(1, 2), (2, 3)}


#### 5. groupby分组


```python
from operator import itemgetter
from itertools import groupby

rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'}, {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'}, {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'}, {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'}, {'address': '1039 W GRANVILLE', 'date': '07/04/2012'}, ]

# groupby() 函数扫描整个序列并且查找连续相同值(或者根据指定key函数返回值相同)的元素序列，所以先要排序
rows.sort(key=itemgetter('date'))  # 先排序，再分组
for date, iterm in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in iterm:
        print (i)
```

    07/01/2012
    {'address': '5412 N CLARK', 'date': '07/01/2012'}
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'}
    07/02/2012
    {'address': '5800 E 58TH', 'date': '07/02/2012'}
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'}
    {'address': '1060 W ADDISON', 'date': '07/02/2012'}
    07/03/2012
    {'address': '2122 N CLARK', 'date': '07/03/2012'}
    07/04/2012
    {'address': '5148 N CLARK', 'date': '07/04/2012'}
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'}



```python
from collections import defaultdict

# 不关心（date）顺序，则可以用下面的分组方式，而且速度更快
rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)
print(rows_by_date)
```

    defaultdict(<class 'list'>, {'07/01/2012': [{'address': '5412 N CLARK', 'date': '07/01/2012'}, {'address': '4801 N BROADWAY', 'date': '07/01/2012'}], '07/02/2012': [{'address': '5800 E 58TH', 'date': '07/02/2012'}, {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'}, {'address': '1060 W ADDISON', 'date': '07/02/2012'}], '07/03/2012': [{'address': '2122 N CLARK', 'date': '07/03/2012'}], '07/04/2012': [{'address': '5148 N CLARK', 'date': '07/04/2012'}, {'address': '1039 W GRANVILLE', 'date': '07/04/2012'}]})


#### 6. 习惯用生成器表达式代替列表生成式，特别在数据量大的情况


```python
print([i**2 for i in range(10)])
print((i**2 for i in range(10)))  # 生成器表达式
```

    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    <generator object <genexpr> at 0x106858570>


#### 7. 生成器表达式参数在某些函数上直接传递(min,max,sum,any,all...)


```python
lst = [1, 3, 5, 7, 9]
print(sum(x**2 for x in lst))  # 平方和

import os
files = os.listdir(os.getcwd())
print(any(name.endswith('.ipynb') for name in files))  # 判断是否存在IPython notebook文件
```

    165
    True

