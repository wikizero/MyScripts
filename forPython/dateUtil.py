# coding:utf-8
'''
    获取一段时间序列
'''
from dateutil.rrule import rrule, MINUTELY, SECONDLY, DAILY, HOURLY, MONTHLY, YEARLY
from dateutil.parser import parse


# dateutil文档 http://dateutil.readthedocs.io/en/stable/rrule.html

class DateUtil():

    def __init__(self):
        self.dimension = {
            'S': SECONDLY,
            'M': MINUTELY,
            'H': HOURLY,
            'D': DAILY,
            'm': MONTHLY,
            'y': YEARLY
        }

    def dt_range(self, start, end, freq, interval):

        if freq not in self.dimension:
            raise Exception('error freq')

        return list(rrule(dtstart=parse(start), until=parse(end), freq=self.dimension[freq], interval=int(interval)))

    def dt_add(self, start, freq, interval):
        if freq not in self.dimension:
            raise Exception('error freq')

        return list(rrule(dtstart=parse(start), freq=self.dimension[freq], interval=int(interval), count=2))[-1]


if __name__ == '__main__':
    dt = DateUtil()
    print dt.dt_range(start='2018-12-1 18:12:30', end='2018-12-1 20:12:30', freq='M', interval=10)
    print dt.dt_add(start='2018-12-1 18:12:30', freq='H', interval=10)
