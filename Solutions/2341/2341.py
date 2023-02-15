# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2023/2/16 06:21
# File: 2341.py
# Desc: 


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        ret = [0,0]
        c = collections.Counter(nums).values()
        for i in c:
            ret[0] += i // 2
            ret[1] += i % 2
        return ret
