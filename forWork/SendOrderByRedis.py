# coding: utf-8
import redis
from pprint import pprint
from datetime import datetime


class SendOrderByRedis:
    def __init__(self):
        self.redis_con = redis.Redis()
        self.channel = 'Order'
        self.order_cfg = {}

    def public(self, channel, msg):
        return self.redis_con.publish(channel, msg)

    def subscribe(self, channel):
        pub = self.redis_con.pubsub()
        pub.subscribe(channel)
        pub.parse_response()
        return pub.parse_response()

    def register(self, order):
        '''
        decorator for register the order
        :param order: maybe it call command
        :return:
        '''
        def inner(func):
            self.order_cfg[order] = func
        return inner

    def send(self, order):
        '''
        send the order to
        :param order:
        :return:
        '''
        return self.public(self.channel, order)

    def start(self):
        print u'Registering the order...'
        pprint(self.order_cfg)
        print u'Waiting for the order...'

        while True:
            try:
                types, channel, order = self.subscribe(self.channel)
                print 'Received an order: {order}'.format(order=order)
                if order not in self.order_cfg:
                    print u'Invalid order!'

                self.order_cfg[order]()

            except Exception as e:
                print e


if __name__ == '__main__':
    pass