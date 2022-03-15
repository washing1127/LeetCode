# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/3/15 10:55
# File: 2044.py
# Desc: CV

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxOr, cnt = 0, 0
        for i in range(1, 1 << len(nums)):
            orVal = reduce(or_, (num for j, num in enumerate(nums) if (i >> j) & 1), 0)
            if orVal > maxOr:
                maxOr, cnt = orVal, 1
            elif orVal == maxOr:
                cnt += 1
        return cnt

