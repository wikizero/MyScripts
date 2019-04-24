# coding:utf-8

lst = [[1,3],[2,6],[8,10],[15,18]]
# lst = [[1,6],[8,10],[15,18]]
# lst = [[1,4],[4,5]]
lst = [[1, 4], [2, 3]]

ret = []
temp = None
for idx, v in enumerate(lst):
    if not temp:
        temp = v
        continue

    x, y = temp
    i, j = v
    if x <= i <= y and i <= y <= j:
        temp = [x, j]
    else:
        ret.append(temp)
        temp = v

ret.append(temp)

print(ret)

lst = [[1, 4], [2, 3]]


# lst = [[1, 3], [2, 6], [8, 10], [15, 18]]


# lst = [[1, 4], [4, 5]]


def merge(intervals):
    if len(intervals) < 2:
        return intervals
    intervals.sort(key=lambda x: x[0])

    ret = []
    temp = intervals[0]
    _len = len(intervals) - 1
    for idx, item in enumerate(intervals[1:], start=1):
        if item[0] <= temp[1] < item[1]:
            print('-')
            temp[1] = item[1]  # temp = [temp[0], item[1]]
        else:
            print('+')
            ret.append(temp)
            temp = item

    return ret


print(merge(lst))
