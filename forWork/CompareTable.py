"""
@Vance
2020-03-19

对比两个csv文件的区别（Pandas无法完成 0与0.0 或 数字与字符数字 的对比）
+--------------+----------------+
|  AGE_AB_DEMO |  "AGE_AB_DEMO" |
+--------------+----------------+
|      40      |      "40"      |
|      22      |      "22"      |
|      18      |      "18"      |
|      0       |      0.0       |
|      47      |      "47"      |
+--------------+----------------+
"""
import prettytable as pt
from itertools import compress


def read_table(filepath, sep=',', header=1):
    data = []
    with open(filepath) as fp:
        for line in fp:
            data.append(line.strip('\n').split(sep))
    columns = data[header - 1]
    data = data[header:]
    return columns, data


def compare(row_limit=10):
    h1, t1 = read_table('table1.csv', header=4)
    h2, t2 = read_table('table2.csv')

    if len(h1) != len(h2):
        raise Exception('len1 != len2')

    rev_data1 = list(zip(*t1))
    rev_data2 = list(zip(*t2))

    not_equal_lst = [map(lambda i, j: i != j, x, y) for x, y in zip(rev_data1, rev_data2)]

    for idx, flag in enumerate(not_equal_lst):
        flag = list(flag)
        if any(flag):
            tb = pt.PrettyTable()
            tb.field_names = [h1[idx], h2[idx]]

            data = list(zip(compress(rev_data1[idx], flag), compress(rev_data2[idx], flag)))[:row_limit]
            for row in data:
                tb.add_row(row)
            print(tb)


if __name__ == '__main__':
    compare(row_limit=5)
