# coding:utf-8
import os
import re


# (1)正则分割字符串
line = 'asa jdf; edu, sdk,dfa, foo'
print re.split(r'[;,\s]\s*', line)

# (2)字符串开头或结尾匹配
# str.startswith('http:') str.endswith('.txt')
files = ['python.py', 'test.xlsx', 'test.txt']
print [f for f in files if f.endswith(('.py', '.txt'))]
# 检查某文件夹下是否含有python文件以及java文件
# any(name.endswith(('.py', '.java')) for name in os.listdir('dir'))

# (3)用 Shell 通配符匹配字符串
from fnmatch import fnmatch, fnmatchcase
names = ['slt1.log', 'slt2.log', 'slt3.log', 'slt.py']
print [name for name in names if fnmatchcase(name, 'slt[1-2].log')]
# fnmatchcase大小写敏感， fnmatch大小写是否敏感依平台而定，建议用fnmatchcase

# (4)re.sub中的第二个参数，可以是一个函数
s = '12 hello 89 world'
print re.sub(r'\d+', lambda x: str(int(x.group())*2), s)  # 将匹配到的数值翻倍
print re.subn(r'\d+', lambda x: str(int(x.group())*2), s)  # re.subn()可以返回替换发生的次数

# (5)字符串对其操作  ljust() , rjust() 和 center()
text = 'code'
print text.center(20, '-')
print format(text, '-^20')  # format()功能强大，可以替代%操作符
print '4326'.zfill(6)  # 顺便提一下补0的函数

# (6)以指定列宽格式化字符串
import textwrap
textwrap.fill(s, 70)