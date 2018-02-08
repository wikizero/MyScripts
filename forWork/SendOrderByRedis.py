# coding: utf-8
import redis
from pprint import pprint
from datetime import datetime
import json


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

    def send(self, order, **params):
        '''
        send the order
        :param order:
        :return:
        '''
        msg = order + '&' + json.dumps(params)
        return self.public(self.channel, msg)

    def start(self):
        print u'Registering the order...'
        pprint(self.order_cfg)
        print u'Waiting for the order...'

        while True:
            try:
                types, channel, msg = self.subscribe(self.channel)
                order, params_json = msg.split('&', 1)
                params = json.loads(params_json) if params_json else None

                print 'Received an order: {order}'.format(order=order)
                if order not in self.order_cfg:
                    print u'Invalid order!'
                else:
                    if params:
                        self.order_cfg[order](**params)
                    else:
                        self.order_cfg[order]()

            except Exception as e:
                print e


if __name__ == '__main__':
    pass