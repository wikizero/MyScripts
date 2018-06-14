# coding:utf-8
from wrapcache import wrapcache

dct = {
    'type': 'iptv',
    'filter': {
        'type': 'tv',
        'nums': {
            'num1': 90,
            'num2': {
                'n1': 1,
                'n2': 2
            }
        }
    },
    'params': [
        {
            'opt': 'create'
        },
        {
            'opt': [
                {'n1': 1},
                {'n2': 2}
            ]
        }
    ]
}

@wrapcache(timeout=10)
def func(dct):
    ret = {}
    for k, v in dct.items():
        k = str(k)
        if isinstance(v, dict):
            temp = {k+'.'+_k: _v for _k,  _v in func(v).items()}
            ret.update(temp)
        elif isinstance(v, list):
            temp = {k+'.'+_k: _v for _k, _v in func(dict(enumerate(v))).items()}
            ret.update(temp)
        else:
            ret[k] = v
    return ret

print func(dct)

{
    'params.1.opt.1.n2': 2,
    'filter.nums.num2.n2': 2,
    'params.0.opt': 'create',
    'params.1.opt.0.n1': 1,
    'type': 'iptv',
    'filter.nums.num2.n1': 1,
    'filter.nums.num1': 90,
    'filter.type': 'tv'
}
