# coding:utf-8

nums = [1, 2, 3, 4, 5]


def func(nums):
    if len(nums) < 3:
        return False

    _min = nums[0]
    for idx, val in enumerate(nums):
        if val > _min:
            if max(nums[idx:]) > val:
                return True
        elif val < _min:
            _min = val

    return False


print func([0,4,2,1,4,-1,9])
