

```python
from models import *
from pprint import pprint

#  我们先看看数据集，这里面有两百条数据
persons = Person.select()
print(u'数据集数量:', persons.count())

# 查看两条数据, 我们知道它包含了主键id就好
two_rows = persons.dicts()[:2]  # 下面的insert操作都会用到这个two_rows变量
pprint(two_rows) 
```

    数据集数量: 200
    [{'brain': 100,
      'color': '橙',
      'country': '蜀',
      'courage': 90,
      'defense': 27,
      'id': 1,
      'name': '诸葛亮',
      'power': 93,
      'speed': 20},
     {'brain': 85,
      'color': '橙',
      'country': '蜀',
      'courage': 95,
      'defense': 31,
      'id': 2,
      'name': '马超',
      'power': 92,
      'speed': 20}]


 如果取出两条数据又直接Person表，这会引发主键重复的异常，如下面所示


```python
try:
    Person.insert_many(two_rows).execute()
except Exception as e:
    print(e)
```

    UNIQUE constraint failed: person.id


在平常工作中insert的时候主键重复我们一般采用两种方式解决：

- insert ignore   (忽略主键重复的该条数据)
- replace into  （替换数据库中的数据，其实是delete、insert结合完成的替换）

<br/>下面就简单介绍在Peewee中如何实现这两种操作

### 1. insert ignore


```python
from peewee import InsertQuery

# insertQuery() 
InsertQuery(Person, rows=two_rows).on_conflict('IGNORE').execute()

# insert_many()
Person.insert_many(two_rows).on_conflict('IGNORE').execute()
```




    True



on_conflict()除了可以接收‘IGNORE’参数，还支持其他的：
- ROLLBACK  （回滚）
- ABORT  （停止）
- FAIL  （报错、抛异常）
- IGNORE  （insert ignore）
- REPLACE  （replace into）

经测试，好像FAIL跟ABORT没有区别...

### 2. replace into


```python
# 正如上面所述，可以使用on_conflict()
Person.insert_many(two_rows).on_conflict('REPLACE').execute()
```




    True



除了使用on_conflict() 还可以使用upsert(), 官方文档是这么解析该函数的：

> Perform an INSERT OR REPLACE query with SQLite. MySQL databases will issue a REPLACE query.


```python
# MySQL中使用upsert()做replace into操作
Person.insert_many(two_rows).upsert().execute()
```




    True


