# coding:utf-8
'''
    ** 格式化粘贴板的数据 **
    1、转成list、dict、dataFrame、json等格式，转指定格式后可以直接赋值给变量
    2、支持导出文件，支持文件格式包括普通文本、csv、excel等
    3、支持生成Python代码，list、dict、dataFrame、json等Python代码生成

'''
import re
import json
from collections import deque
import pandas as pd
import pyperclip
from bs4 import BeautifulSoup


def get_text():
    """
    get text from clipboard
    :return:
    """
    text = pyperclip.paste()
    if not text.strip():
        raise Exception('Nothing in your clipboard')
    return text


def format_(fm, sep=None, filter=None, **param):
    """
    :param fm: 'list', 'df', 'dict'

    指定df可选参数: encoding 编码
                  index_col 第几行做索引
                  names 字段名

    指定list可选参数: sep 分隔符(支持正则)
                    maxsplit,flag 用法参考re.split
                    filter: 'odd', 'even'

    :return: type of fm
    """
    if fm == 'df':
        return pd.read_clipboard(**param)
    elif fm == 'list':
        if not sep:
            sep = '\s+'
        lst = re.split(pattern=sep, string=get_text(), **param)
        if filter:
            if filter == 'even':
                lst = [item for index, item in enumerate(lst) if (index+1) % 2 == 0]
            elif filter == 'odd':
                lst = [item for index, item in enumerate(lst) if (index+1) % 2 != 0]
        return lst


def out(content, filename):
    """
    dict: json, plain text, excel
    df: excel, csv, plain text
    list: plain text
    """
    if filename.endswith('.xlsx'):
        with pd.ExcelWriter(filename) as writer:
            content.to_excel(writer, index=None)
            writer.save()
    elif filename.endswith('.csv'):
        pass
    elif filename.endswith('.json'):
        json.dump(content, open(filename, 'w+'))
    else:
        with open(filename, 'w+') as fp:
            fp.write('\n'.join(content))


def handle_http():
    '''
        将网页复制过来的cookies、headers转化成字典
    :return: dict
    '''
    ret = format_('list', sep='\n')
    return dict([i.split(':', 1) for i in ret])


def history():
    dq = deque(10)


if __name__ == '__main__':
    # 读取内存的文件
    # pickup headq
    import uniout
    # print lst
    print format_('list', filter='even')

