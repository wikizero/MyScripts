import re


def func(s):
    print(s.group())
    print(s.group(1))
    print(s.group(2))
    num1, num2 = int(s.group(1)), int(s.group(2))
    return f'{num1}+{num2}={num1 + num2}'


s = '200加300等于多少呢？'
ret = re.sub('(\d+).(\d+).*', r'\1+\2=?', s)
print(ret)

ret = re.sub('(\d+).(\d+).*', func, s)
print(ret)
