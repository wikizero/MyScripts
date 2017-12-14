# coding:utf-8
import pandas as pd
import pyperclip


def get_text():
    """
    get text from clipboard
    :return:
    """
    text = pyperclip.paste()
    if not text.strip():
        raise Exception('Nothing in your clipboard')
    return text


def _format(fm, **param):
    """
    :param fm: ['list', 'df', 'dict']
    :return:
    """
    if fm == 'df':
        return pd.read_clipboard(**param)
    elif fm == 'list':
        return get_text().split()


if __name__ == '__main__':
    print _format('list', header=None)