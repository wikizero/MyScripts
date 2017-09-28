# coding:utf-8
import pandas as pd


def merge_col(frame, func=None, symbol=''):
    row, col = frame.shape
    if col < 2:
        raise Exception(u'DataFrame至少两列以上才能拼接')

    ret = frame.apply(lambda x: symbol.join(map(str, x)), axis=1)
    return ret.apply(func) if func else ret


if __name__ == '__main__':

    df = pd.DataFrame(data=[['A', 'B', 3, 'R'], ['T', 'Y', 9, 'P']], columns=['a', 'b', 'c', 'd'])
    print merge_col(df, str.lower, '_')

