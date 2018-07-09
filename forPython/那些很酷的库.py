# coding:utf-8

# （1）异常重试  官方例子：https://pypi.python.org/pypi/retry/
from retry import retry
@retry()
def make_trouble():
    print 'func...'
    print 1/0

# （2）文件下载
import wget
# wget.download("http://www.cnn.com/")

# （3）对字符串进行模糊匹配的库
from fuzzywuzzy import fuzz
print fuzz.ratio("Hit me haha", "Hit me ha")

# (4)中文打印
import uniout  # 引进来即可
print [u'哈啊', '']


# (5)
lst = range(10)
for i in lst:
    if i % 2 == 0:
        lst.append(5)
    print i


