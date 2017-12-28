# coding: utf-8
import redis
import time

redis_con = redis.Redis()


def public(channel, msg):
    redis_con.publish(channel, msg)


def subscribe(channel):
    pub = redis_con.pubsub()
    pub.subscribe(channel)
    pub.parse_response()
    return pub


if __name__ == '__main__':
    # 订阅
    # while True:
    #     data = subscribe('A')
    #     print data.parse_response()

    # 发布
    public('A', '啥东西嘛')