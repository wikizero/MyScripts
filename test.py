# coding:utf-8
import requests

import redis

#  任务扔进redis队列  需要不需要序列化（意味着取出来也需要反序列化） （丢任务，优先级） 任务丢到111服务器 大家从111上拉取
#  从redis拉取任务（考虑线程安全）
# 高级：如何监听redis 是否有任务，工人便开始工作



