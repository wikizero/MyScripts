import time
from datetime import datetime
from bisect import bisect_left

from dateutil.parser import parse


def ftime(dt, interval, opt):
    """
    时间向上、向下取整或四舍五入操作
    :param dt: 传入的时间 字符串/datetime格式
    :param interval: 时间颗粒度 以秒为单位
    :param opt: ceil floor round
    :return: datetime
    """
    basic_stamp = 1514736000  # 2018-01-01

    if opt not in ['ceil', 'floor', 'round']:
        raise Exception('error opt')

    stamp = int(dt.timestamp() if isinstance(dt, datetime) else parse(dt).timestamp())
    stamp_lst = list(range(basic_stamp, int(time.time()), interval))  # 生成时间戳列表
    mod = (stamp - basic_stamp) % interval

    pos = bisect_left(stamp_lst, stamp)  # 获取插入时间列表的位置

    if mod and opt == 'floor':
        pos += -1
    elif opt == 'round' and mod < interval / 2:
        pos += -1

    return datetime.fromtimestamp(stamp_lst[pos])


if __name__ == '__main__':
    print(ftime('2018-08-09 09:44:30', 600, 'round'))
