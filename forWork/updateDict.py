def move(data: dict, motion: dict):
    """
    将字典的键值对进行移动， 可以同时多对进行移动 (类似Linux的mv， 可以重命名)
    :param data:
    :param motion: {newKeyStr: oldKeyStr}
    :return:
    """
    for new, old in motion.items():
        execute = f"data{''.join([str([i]) for i in old.split('.')])}"
        # 获取旧的键的值
        val = eval(execute)

        k_execute = f"data{''.join([str([i]) for i in new.split('.')])} = {val}"
        # 将旧的键的值赋给新键
        exec(k_execute)

        # 删除旧的键
        delete(data, [old])

    return data


def delete(data: dict, keys: list):
    """
    删除某些键
    :param data:
    :param keys:
    :return:
    """
    for key_chain in keys:
        ks = key_chain.split('.')
        execute = f"del data{''.join([str([i]) for i in ks])}"
        print(execute)

        try:
            exec(execute)
        except Exception as e:
            pass

    return data


if __name__ == '__main__':
    # TODO 需不需要做一个根据 key.key.[index].key 来索引数据的工具
    # TODO 了解整理 from collections import defaultdict
    dct = {
        'baseInfo': {
            'name': {
                'firstName': '$#$#%',
                'lastName': '*&*^*'
            },
            'age': 18,
            'hobby': ['movie', 'music']
        },
        'detail': {
            'phone': 1378172831,
            'address': 'xxx'
        }
    }
    # print('abc'.split('.'))  # ['abc']

    # lst = [2, 3, 2, 4, 5, 1, 2]
    # print({i for i in lst})  # 集合表达式

    # ret = delete(dct, ['baseInfo.name.lastName', 'baseInfo.hobby', 'detail'])
    # print(ret)

    # execute = f"dct['baseInfo']['hobby']"
    # print(eval(execute))

    # from collections import defaultdict
    # print(defaultdict(dict))

    print(move(dct, {'baseInfos': 'baseInfo'}))
