# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2020/12/7 11:31
# File: 0001.py
# Desc: 


class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        dic = {nums[0]: 0}
        for idx, num in enumerate(nums[1:]):
            n = target - num
            if n not in dic:
                dic[num] = idx + 1
            else:
                return [dic[n], idx + 1]
