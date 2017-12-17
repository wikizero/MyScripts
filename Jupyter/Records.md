

```python
import records
from pyecharts import Pie, Bar, Page

db = records.Database('mysql://root:root@39.108.141.110:3306/Jobs')
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




<script>
    require.config({
         paths:{
           'echarts': '/nbextensions/echarts/echarts.min'
         }
    });
</script>
<div id="8baf36541938410d8a1c93138391f862" style="width:800px; height:400px;"></div>

<script>
    require([ 'echarts' ],function(ec){
	var myChart = ec.init(document.getElementById('8baf36541938410d8a1c93138391f862'));
var option =  {
    "title": [
        {
            "text": "Pie",
            "subtext": "",
            "left": "auto",
            "top": "auto",
            "textStyle": {
                "color": "#000",
                "fontSize": 18
            },
            "subtextStyle": {
                "color": "#aaa",
                "fontSize": 12
            }
        }
    ],
    "toolbox": {
        "show": true,
        "orient": "vertical",
        "left": "95%",
        "top": "center",
        "feature": {
            "saveAsImage": {
                "show": true,
                "title": "\u4e0b\u8f7d\u56fe\u7247"
            },
            "restore": {
                "show": true
            },
            "dataView": {
                "show": true
            }
        }
    },
    "series_id": 1422748,
    "tooltip": {
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "formatter": null,
        "textStyle": {
            "color": "#fff",
            "fontSize": 14
        }
    },
    "series": [
        {
            "type": "pie",
            "name": "\u603b\u6570:8871",
            "data": [
                {
                    "name": "Android",
                    "value": 642
                },
                {
                    "name": "C/C++",
                    "value": 811
                },
                {
                    "name": "iOS",
                    "value": 285
                },
                {
                    "name": "Java",
                    "value": 2701
                },
                {
                    "name": "PHP",
                    "value": 890
                },
                {
                    "name": "Python",
                    "value": 2057
                },
                {
                    "name": "\u5927\u6570\u636e",
                    "value": 3
                },
                {
                    "name": "\u6570\u636e\u5206\u6790",
                    "value": 24
                },
                {
                    "name": "\u6570\u636e\u6316\u6398",
                    "value": 1458
                }
            ],
            "radius": [
                "0%",
                "75%"
            ],
            "center": [
                "50%",
                "50%"
            ],
            "roseType": null,
            "label": {
                "normal": {
                    "show": true,
                    "position": "outside",
                    "textStyle": {
                        "color": "#000",
                        "fontSize": 12
                    },
                    "formatter": "{b}: {d}%"
                },
                "emphasis": {
                    "show": true,
                    "position": null,
                    "textStyle": {
                        "color": "#fff",
                        "fontSize": 12
                    }
                }
            },
            "seriesId": 1422748
        }
    ],
    "legend": [
        {
            "data": [
                "Android",
                "C/C++",
                "iOS",
                "Java",
                "PHP",
                "Python",
                "\u5927\u6570\u636e",
                "\u6570\u636e\u5206\u6790",
                "\u6570\u636e\u6316\u6398"
            ],
            "selectedMode": "multiple",
            "show": true,
            "left": "center",
            "top": "top",
            "orient": "horizontal",
            "textStyle": {
                "fontSize": 12,
                "color": "#333"
            }
        }
    ],
    "backgroundColor": "#fff",
    "color": [
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597",
        "#f6f5ec"
    ]
};
myChart.setOption(option);

    });
</script>




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




<script>
    require.config({
         paths:{
           'echarts': '/nbextensions/echarts/echarts.min'
         }
    });
</script>
<div id="48e5b96f78334793aaed93425174d56f" style="width:800px; height:400px;"></div>

<script>
    require([ 'echarts' ],function(ec){
	var myChart = ec.init(document.getElementById('48e5b96f78334793aaed93425174d56f'));
var option =  {
    "title": [
        {
            "text": "Pie",
            "subtext": "",
            "left": "auto",
            "top": "auto",
            "textStyle": {
                "color": "#000",
                "fontSize": 18
            },
            "subtextStyle": {
                "color": "#aaa",
                "fontSize": 12
            }
        }
    ],
    "toolbox": {
        "show": true,
        "orient": "vertical",
        "left": "95%",
        "top": "center",
        "feature": {
            "saveAsImage": {
                "show": true,
                "title": "\u4e0b\u8f7d\u56fe\u7247"
            },
            "restore": {
                "show": true
            },
            "dataView": {
                "show": true
            }
        }
    },
    "series_id": 1321781,
    "tooltip": {
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "formatter": null,
        "textStyle": {
            "color": "#fff",
            "fontSize": 14
        }
    },
    "series": [
        {
            "type": "pie",
            "name": "",
            "data": [
                {
                    "name": "Python",
                    "value": 1935.0
                },
                {
                    "name": "\u6570\u636e\u6316\u6398",
                    "value": 1421.0
                }
            ],
            "radius": [
                "0%",
                "30%"
            ],
            "center": [
                "50%",
                "50%"
            ],
            "roseType": null,
            "label": {
                "normal": {
                    "show": false,
                    "position": "outside",
                    "textStyle": {
                        "color": "#000",
                        "fontSize": 12
                    },
                    "formatter": "{b}: {d}%"
                },
                "emphasis": {
                    "show": true,
                    "position": null,
                    "textStyle": {
                        "color": "#fff",
                        "fontSize": 12
                    }
                }
            },
            "seriesId": 1321781
        },
        {
            "type": "pie",
            "name": "",
            "data": [
                {
                    "name": "Python_\u5927\u4e13",
                    "value": 320
                },
                {
                    "name": "Python_\u672c\u79d1",
                    "value": 1600
                },
                {
                    "name": "Python_\u7855\u58eb",
                    "value": 15
                },
                {
                    "name": "\u6570\u636e\u6316\u6398_\u535a\u58eb",
                    "value": 2
                },
                {
                    "name": "\u6570\u636e\u6316\u6398_\u5927\u4e13",
                    "value": 39
                },
                {
                    "name": "\u6570\u636e\u6316\u6398_\u672c\u79d1",
                    "value": 1123
                },
                {
                    "name": "\u6570\u636e\u6316\u6398_\u7855\u58eb",
                    "value": 257
                }
            ],
            "radius": [
                "40%",
                "53%"
            ],
            "center": [
                "50%",
                "50%"
            ],
            "roseType": null,
            "label": {
                "normal": {
                    "show": true,
                    "position": "outside",
                    "textStyle": {
                        "color": "#000",
                        "fontSize": 12
                    },
                    "formatter": "{b}: {d}%"
                },
                "emphasis": {
                    "show": true,
                    "position": null,
                    "textStyle": {
                        "color": "#fff",
                        "fontSize": 12
                    }
                }
            },
            "seriesId": 1321781
        }
    ],
    "legend": [
        {
            "data": [
                "Python",
                "\u6570\u636e\u6316\u6398",
                "Python_\u5927\u4e13",
                "Python_\u672c\u79d1",
                "Python_\u7855\u58eb",
                "\u6570\u636e\u6316\u6398_\u535a\u58eb",
                "\u6570\u636e\u6316\u6398_\u5927\u4e13",
                "\u6570\u636e\u6316\u6398_\u672c\u79d1",
                "\u6570\u636e\u6316\u6398_\u7855\u58eb"
            ],
            "selectedMode": "multiple",
            "show": true,
            "left": "center",
            "top": "top",
            "orient": "horizontal",
            "textStyle": {
                "fontSize": 12,
                "color": "#333"
            }
        }
    ],
    "backgroundColor": "#fff",
    "color": [
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597",
        "#f6f5ec"
    ]
};
myChart.setOption(option);

    });
</script>




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




<script>
    require.config({
         paths:{
           'echarts': '/nbextensions/echarts/echarts.min'
         }
    });
</script>
<div id="c7376a0c85244225b9e0f26869e83483" style="width:800px; height:400px;"></div>
<div id="ab50a16b79654a3d9b392013ea0ebfb4" style="width:800px; height:400px;"></div>

<script>
    require([ 'echarts' ],function(ec){
	var myChart = ec.init(document.getElementById('c7376a0c85244225b9e0f26869e83483'));
var option =  {
    "title": [
        {
            "text": "Bar1",
            "subtext": "",
            "left": "auto",
            "top": "auto",
            "textStyle": {
                "color": "#000",
                "fontSize": 18
            },
            "subtextStyle": {
                "color": "#aaa",
                "fontSize": 12
            }
        }
    ],
    "toolbox": {
        "show": true,
        "orient": "vertical",
        "left": "95%",
        "top": "center",
        "feature": {
            "saveAsImage": {
                "show": true,
                "title": "\u4e0b\u8f7d\u56fe\u7247"
            },
            "restore": {
                "show": true
            },
            "dataView": {
                "show": true
            }
        }
    },
    "series_id": 8416578,
    "tooltip": {
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "formatter": null,
        "textStyle": {
            "color": "#fff",
            "fontSize": 14
        }
    },
    "series": [
        {
            "type": "bar",
            "name": "",
            "data": [
                642.0,
                811.0,
                285.0,
                2701.0,
                890.0,
                2057.0,
                3.0,
                24.0,
                1458.0
            ],
            "stack": "",
            "barCategoryGap": "20%",
            "label": {
                "normal": {
                    "show": false,
                    "position": "top",
                    "textStyle": {
                        "color": "#000",
                        "fontSize": 12
                    },
                    "formatter": null
                },
                "emphasis": {
                    "show": true,
                    "position": null,
                    "textStyle": {
                        "color": "#fff",
                        "fontSize": 12
                    }
                }
            },
            "markPoint": {
                "data": [
                    {
                        "type": "max",
                        "name": "Maximum",
                        "valueDim": null,
                        "symbol": "pin",
                        "symbolSize": 50,
                        "label": {
                            "normal": {
                                "textStyle": {
                                    "color": "#fff"
                                }
                            }
                        }
                    },
                    {
                        "type": "min",
                        "name": "Minimum",
                        "valueDim": null,
                        "symbol": "pin",
                        "symbolSize": 50,
                        "label": {
                            "normal": {
                                "textStyle": {
                                    "color": "#fff"
                                }
                            }
                        }
                    }
                ]
            },
            "markLine": {
                "data": []
            },
            "seriesId": 8416578
        }
    ],
    "legend": [
        {
            "data": [
                ""
            ],
            "selectedMode": "multiple",
            "show": true,
            "left": "center",
            "top": "top",
            "orient": "horizontal",
            "textStyle": {
                "fontSize": 12,
                "color": "#333"
            }
        }
    ],
    "backgroundColor": "#fff",
    "xAxis": [
        {
            "name": "",
            "show": true,
            "nameLocation": "middle",
            "nameGap": 25,
            "nameTextStyle": {
                "fontSize": 14
            },
            "axisLabel": {
                "interval": "auto",
                "rotate": 0,
                "margin": 8,
                "textStyle": {
                    "fontSize": 12,
                    "color": "#000"
                }
            },
            "axisTick": {
                "alignWithLabel": false
            },
            "inverse": false,
            "position": null,
            "boundaryGap": true,
            "min": null,
            "max": null,
            "data": [
                "Android",
                "C/C++",
                "iOS",
                "Java",
                "PHP",
                "Python",
                "\u5927\u6570\u636e",
                "\u6570\u636e\u5206\u6790",
                "\u6570\u636e\u6316\u6398"
            ],
            "type": "category"
        }
    ],
    "yAxis": [
        {
            "name": "",
            "show": true,
            "nameLocation": "middle",
            "nameGap": 25,
            "nameTextStyle": {
                "fontSize": 14
            },
            "axisLabel": {
                "formatter": "{value} ",
                "rotate": 0,
                "interval": "auto",
                "margin": 8,
                "textStyle": {
                    "fontSize": 12,
                    "color": "#000"
                }
            },
            "axisTick": {
                "alignWithLabel": false
            },
            "inverse": false,
            "position": null,
            "boundaryGap": true,
            "min": null,
            "max": null,
            "type": "value"
        }
    ],
    "color": [
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597",
        "#f6f5ec"
    ]
};
myChart.setOption(option);
var myChart = ec.init(document.getElementById('ab50a16b79654a3d9b392013ea0ebfb4'));
var option =  {
    "title": [
        {
            "text": "Bar2",
            "subtext": "",
            "left": "auto",
            "top": "auto",
            "textStyle": {
                "color": "#000",
                "fontSize": 18
            },
            "subtextStyle": {
                "color": "#aaa",
                "fontSize": 12
            }
        }
    ],
    "toolbox": {
        "show": true,
        "orient": "vertical",
        "left": "95%",
        "top": "center",
        "feature": {
            "saveAsImage": {
                "show": true,
                "title": "\u4e0b\u8f7d\u56fe\u7247"
            },
            "restore": {
                "show": true
            },
            "dataView": {
                "show": true
            }
        }
    },
    "series_id": 6024759,
    "tooltip": {
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "formatter": null,
        "textStyle": {
            "color": "#fff",
            "fontSize": 14
        }
    },
    "series": [
        {
            "type": "bar",
            "name": "Java",
            "data": [
                270,
                1152,
                439,
                267
            ],
            "stack": "",
            "barCategoryGap": "20%",
            "label": {
                "normal": {
                    "show": false,
                    "position": "top",
                    "textStyle": {
                        "color": "#000",
                        "fontSize": 12
                    },
                    "formatter": null
                },
                "emphasis": {
                    "show": true,
                    "position": null,
                    "textStyle": {
                        "color": "#fff",
                        "fontSize": 12
                    }
                }
            },
            "markPoint": {
                "data": [
                    {
                        "type": "max",
                        "name": "Maximum",
                        "valueDim": null,
                        "symbol": "pin",
                        "symbolSize": 50,
                        "label": {
                            "normal": {
                                "textStyle": {
                                    "color": "#fff"
                                }
                            }
                        }
                    },
                    {
                        "type": "min",
                        "name": "Minimum",
                        "valueDim": null,
                        "symbol": "pin",
                        "symbolSize": 50,
                        "label": {
                            "normal": {
                                "textStyle": {
                                    "color": "#fff"
                                }
                            }
                        }
                    }
                ]
            },
            "markLine": {
                "data": []
            },
            "seriesId": 6024759
        },
        {
            "type": "bar",
            "name": "Python",
            "data": [
                142,
                1090,
                276,
                210
            ],
            "stack": "",
            "barCategoryGap": "20%",
            "label": {
                "normal": {
                    "show": false,
                    "position": "top",
                    "textStyle": {
                        "color": "#000",
                        "fontSize": 12
                    },
                    "formatter": null
                },
                "emphasis": {
                    "show": true,
                    "position": null,
                    "textStyle": {
                        "color": "#fff",
                        "fontSize": 12
                    }
                }
            },
            "markPoint": {
                "data": [
                    {
                        "type": "max",
                        "name": "Maximum",
                        "valueDim": null,
                        "symbol": "pin",
                        "symbolSize": 50,
                        "label": {
                            "normal": {
                                "textStyle": {
                                    "color": "#fff"
                                }
                            }
                        }
                    },
                    {
                        "type": "min",
                        "name": "Minimum",
                        "valueDim": null,
                        "symbol": "pin",
                        "symbolSize": 50,
                        "label": {
                            "normal": {
                                "textStyle": {
                                    "color": "#fff"
                                }
                            }
                        }
                    }
                ]
            },
            "markLine": {
                "data": []
            },
            "seriesId": 6024759
        },
        {
            "type": "bar",
            "name": "\u6570\u636e\u6316\u6398",
            "data": [
                135,
                826,
                186,
                114
            ],
            "stack": "",
            "barCategoryGap": "20%",
            "label": {
                "normal": {
                    "show": false,
                    "position": "top",
                    "textStyle": {
                        "color": "#000",
                        "fontSize": 12
                    },
                    "formatter": null
                },
                "emphasis": {
                    "show": true,
                    "position": null,
                    "textStyle": {
                        "color": "#fff",
                        "fontSize": 12
                    }
                }
            },
            "markPoint": {
                "data": [
                    {
                        "type": "max",
                        "name": "Maximum",
                        "valueDim": null,
                        "symbol": "pin",
                        "symbolSize": 50,
                        "label": {
                            "normal": {
                                "textStyle": {
                                    "color": "#fff"
                                }
                            }
                        }
                    },
                    {
                        "type": "min",
                        "name": "Minimum",
                        "valueDim": null,
                        "symbol": "pin",
                        "symbolSize": 50,
                        "label": {
                            "normal": {
                                "textStyle": {
                                    "color": "#fff"
                                }
                            }
                        }
                    }
                ]
            },
            "markLine": {
                "data": []
            },
            "seriesId": 6024759
        }
    ],
    "legend": [
        {
            "data": [
                "Java",
                "Python",
                "\u6570\u636e\u6316\u6398"
            ],
            "selectedMode": "multiple",
            "show": true,
            "left": "center",
            "top": "top",
            "orient": "horizontal",
            "textStyle": {
                "fontSize": 12,
                "color": "#333"
            }
        }
    ],
    "backgroundColor": "#fff",
    "xAxis": [
        {
            "name": "",
            "show": true,
            "nameLocation": "middle",
            "nameGap": 25,
            "nameTextStyle": {
                "fontSize": 14
            },
            "axisLabel": {
                "interval": "auto",
                "rotate": 0,
                "margin": 8,
                "textStyle": {
                    "fontSize": 12,
                    "color": "#000"
                }
            },
            "axisTick": {
                "alignWithLabel": false
            },
            "inverse": false,
            "position": null,
            "boundaryGap": true,
            "min": null,
            "max": null,
            "data": [
                "\u676d\u5dde",
                "\u5317\u4eac",
                "\u4e0a\u6d77",
                "\u6df1\u5733"
            ],
            "type": "category"
        }
    ],
    "yAxis": [
        {
            "name": "",
            "show": true,
            "nameLocation": "middle",
            "nameGap": 25,
            "nameTextStyle": {
                "fontSize": 14
            },
            "axisLabel": {
                "formatter": "{value} ",
                "rotate": 0,
                "interval": "auto",
                "margin": 8,
                "textStyle": {
                    "fontSize": 12,
                    "color": "#000"
                }
            },
            "axisTick": {
                "alignWithLabel": false
            },
            "inverse": false,
            "position": null,
            "boundaryGap": true,
            "min": null,
            "max": null,
            "type": "value"
        }
    ],
    "color": [
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597",
        "#f6f5ec"
    ]
};
myChart.setOption(option);

    });
</script>



