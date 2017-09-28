# coding:utf-8
import hashlib


def md5_encode(s):
    m = hashlib.md5()
    m.update(s)
    return m.hexdigest()