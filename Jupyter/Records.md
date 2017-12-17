

```python
import records
from pyecharts import Pie, Bar, Page

db = records.Database('mysql://user:pw@ip:3306/db')
```

#### 1. 饼图


```python
def show_pie(db, sql, title='Pie'):
    rows = db.query(sql)
    df = rows.export('df')
    columns = df.columns.tolist()
    labels, datas = df[columns[0]], df[columns[1]]
    pie = Pie(title)
    pie.add('总数:{sum}'.format(sum=sum(datas)), labels, datas, is_label_show=True)
    return pie
    
sql = "select type, count(*) as count from jobanalysis where type !='' group by type"
show_pie(db, sql)
```








#### 2. 环形图



```python
def show_pie2(db, sql, title='Pie'):
    rows = db.query(sql)
    df = rows.export('df')
    columns = df.columns.tolist()
    out_labels, counts = df[columns[1]], df[columns[2]]
    
    inner_data = {}
    for key, item in df.groupby(columns[0]):
        inner_data[key] = item[columns[2]].sum()
        
    pie = Pie(title)
    pie.add('', inner_data.keys(), inner_data.values(), radius=[0, 30], legend_orient='vertical', legend_pos='left')
    pie.add('', out_labels, counts, radius=[40, 53], is_label_show=True)

    return pie

sql = "select type, concat(type,'_',edu), count(2) as count from jobanalysis where type in ('Python', '数据挖掘') and edu!='不限' group by type, edu"
show_pie2(db, sql, title='Pie')
```









#### 3. 柱状图


```python
def show_bar(db, sql, title='Bar'):
    rows = db.query(sql)
    df = rows.export('df')
    columns = df.columns.tolist()
    row, col = df.shape
    bar = Bar(title)
    
    if col == 2:
        labels, counts = df[columns[0]], df[columns[1]]
        bar.add('', labels, counts, mark_point=["max", "min"])
    
    elif col == 3:
        labels = list(set(df[columns[1]]))
        for key, item in df.groupby(columns[0]):
            dct = dict(zip(item[columns[1]], item[columns[2]]))
            data = [dct.get(label, 0) for label in labels]
            bar.add(key, labels, data, mark_point=["max", "min"])
            
    return bar

page = Page()
sql = "select type, count(*) as count from jobanalysis where type !='' group by type"
page.add(show_bar(db, sql, 'Bar1'))

sql = "select * from (select type, address, count(*) as count from jobanalysis where type in ('Python', 'Java', '数据挖掘') group by type, address) temp where temp.count > 100"
page.add(show_bar(db, sql, 'Bar2'))

page
```







