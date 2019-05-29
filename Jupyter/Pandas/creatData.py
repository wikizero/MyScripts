import numpy as np
import pandas as pd
from faker import Faker


def random_data(row_num, csv_filename='data.csv'):
    """
    生成随机数据，包含以下数据
    datetime, ip, city, method, module, browser

    :param row_num: 生成数据的行数
    :param csv_filename: 导出csv文件名
    :return: None
    """
    f = Faker(locale='zh_CN')

    random_ip = [f.ipv4() for i in range(100)]
    random_city = [f.city() for i in range(20)]
    browsers = ['chrome', 'firefox', 'safari', 'ie']
    methods = ['get', 'post', 'delete', 'option', 'put']
    modules = ['主页', '任务列表', '任务详情', '项目列表', '项目详情', '个人信息']

    df = pd.DataFrame({
        'datetime': [f.past_datetime('-10d') for i in range(row_num)],
        'ip': np.random.choice(random_ip, row_num),
        'city': np.random.choice(random_city, row_num),
        'method': np.random.choice(methods, row_num),
        'module': np.random.choice(modules, row_num),
        'browser': np.random.choice(browsers, row_num),
    })

    # 打印前10行，看效果
    print(df.head())

    df.to_csv(csv_filename, index=False)


random_data(10000)
