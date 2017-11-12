# coding:utf-8
import random

# （1）四舍五入函数作用在个位、十位、百位、、、
print round(14558, -1)

# （2）随机数生成
print random.randint(1, 11)  # 随机整数
print random.random()  # 随机浮点数 0-1

# (3) 随机选择
print random.choice(xrange(10))  # 给定序列随机取出一个元素
print random.sample(range(10), 3)  # 给定序列随机取出n个
lst = list(xrange(10))
random.shuffle(lst)  # 随机打乱给定序列的元素的顺序
