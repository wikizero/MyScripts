
#### Pandas分组函数的[官方文档](http://pandas.pydata.org/pandas-docs/stable/groupby.html) 


```python
import pandas as pd
import numpy as np

df = pd.DataFrame({'key1':list('aabba'),
                  'key2': ['one','two','one','two','one'],
                  'data1': np.random.randn(5),
                  'data2': np.random.randn(5)})

df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>data1</th>
      <th>data2</th>
      <th>key1</th>
      <th>key2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.277727</td>
      <td>-0.997998</td>
      <td>a</td>
      <td>one</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-0.066114</td>
      <td>0.284571</td>
      <td>a</td>
      <td>two</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-0.442184</td>
      <td>0.873477</td>
      <td>b</td>
      <td>one</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-0.136016</td>
      <td>-0.693264</td>
      <td>b</td>
      <td>two</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-0.969612</td>
      <td>-0.153111</td>
      <td>a</td>
      <td>one</td>
    </tr>
  </tbody>
</table>
</div>



#### 1. groupby 进行数据分组的简单应用


```python
for key, item in df.groupby('key2'):  # 还可以同时对两个字段分组如参数 ['key2', 'key1']
    print(key)
    print(item)  # DataFrame
```

    one
          data1     data2 key1 key2
    0  0.277727 -0.997998    a  one
    2 -0.442184  0.873477    b  one
    4 -0.969612 -0.153111    a  one
    two
          data1     data2 key1 key2
    1 -0.066114  0.284571    a  two
    3 -0.136016 -0.693264    b  two



```python
# groupby默认是在axis=0上进行分组的，通过设置也可以在其他任何轴上进行分组
for key, item in df.groupby(df.dtypes, axis=1): # 按数据类型分组
    print(key)
    print(item)  # DataFrame
```

    float64
          data1     data2
    0  0.277727 -0.997998
    1 -0.066114  0.284571
    2 -0.442184  0.873477
    3 -0.136016 -0.693264
    4 -0.969612 -0.153111
    object
      key1 key2
    0    a  one
    1    a  two
    2    b  one
    3    b  two
    4    a  one


#### 2. 通过字典或者series进行分组


```python
mapping = {'data1': 'data', 'data2': 'data', 'key1': 'key', 'key2': 'key'}
for key, item in df.groupby(mapping, axis=1): 
    print(key)
    print(item) 
```

    data
          data1     data2
    0  0.277727 -0.997998
    1 -0.066114  0.284571
    2 -0.442184  0.873477
    3 -0.136016 -0.693264
    4 -0.969612 -0.153111
    key
      key1 key2
    0    a  one
    1    a  two
    2    b  one
    3    b  two
    4    a  one


#### 3. 通过函数进行分组


```python
# 奇数与偶数行分组
for key, item in df.groupby(lambda x: int(x) % 2 == 0, axis=0): 
    print(key)
    print(item) 
```

    False
          data1     data2 key1 key2
    1 -0.066114  0.284571    a  two
    3 -0.136016 -0.693264    b  two
    True
          data1     data2 key1 key2
    0  0.277727 -0.997998    a  one
    2 -0.442184  0.873477    b  one
    4 -0.969612 -0.153111    a  one


#### 小例子


```python
cols = ['流水号', '处理人', '处理时间']
data = [[10000, '张三', '2016-10-01'],
        [10000, '李四', '2016-10-02'],
        [10001, '王五', '2016-10-01'],
        [10002, '赵六', '2016-10-03'],
        [10001, '黄七', '2016-10-02'],
        [10000, '吴八', '2016-10-03']]
frame = pd.DataFrame(data,columns=cols)

def combination(names):
    return ','.join(names)
    
frame.groupby('流水号').aggregate(combination)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>处理人</th>
      <th>处理时间</th>
    </tr>
    <tr>
      <th>流水号</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>10000</th>
      <td>张三,李四,吴八</td>
      <td>2016-10-01,2016-10-02,2016-10-03</td>
    </tr>
    <tr>
      <th>10001</th>
      <td>王五,黄七</td>
      <td>2016-10-01,2016-10-02</td>
    </tr>
    <tr>
      <th>10002</th>
      <td>赵六</td>
      <td>2016-10-03</td>
    </tr>
  </tbody>
</table>
</div>


