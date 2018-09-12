from multiprocessing.dummy import Pool
import time
from datetime import datetime


def multiprocess(data, group=0, processes=5):
    """
    通过装饰器修饰获得多线程处理能力
    :param data: 需要处理的数据
    :param group: 是否对数据进行分组，0为不分组，其他自然数则为分组时每组数据的数量
    :param processes: 线程数量
    :return: 处理结果
    """

    # TODO map_async chunkSize
    # TODO data传入生成器如何处理
    def decorator(func):
        def wrapper(*args, **kwargs):
            rows = data
            start = time.time()
            print(f'Multiprocess >> data length:{len(rows)}, group:{group}, processes:{processes}')

            if group:
                rows = [rows[i:i + group] for i in range(0, len(rows), group)]

            ret = Pool(processes).map(func, rows)

            print(f'Multiprocess >> spend time:{time.time() - start} seconds')
            return ret

        return wrapper

    return decorator


data1 = list('ABCDEFGUYUGHPMQW')


@multiprocess(data1, processes=20)
def test1(word):
    print(f'word:{word}')
    time.sleep(5)
    print(datetime.now())


data2 = list(range(20000000))


@multiprocess(data2, group=100000, processes=5)
def test2(num):
    print(f'insert success len:{len(num)}')
    # for i in num:
    time.sleep(0.1)


if __name__ == '__main__':
    # test1()
    test2()
