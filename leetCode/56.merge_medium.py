# coding:utf-8

 # [[1,3],[2,6],[8,10],[15,18]]
 # [[1,6],[8,10],[15,18]]
lst = [[1,4],[4,5]]

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

print ret