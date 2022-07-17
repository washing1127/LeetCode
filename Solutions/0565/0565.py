# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/7/17 20:37
# File: 0565.py
# Desc: 

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        self.s = set()
        def parse(idx):
            ret = 0
            s = set()
            while idx not in s:
                s.add(idx)
                self.s.add(idx)
                idx = nums[idx]
                ret += 1
            return ret
        ret = 0
        for idx in range(len(nums)):
            if idx in self.s: continue
            # print(idx, parse(idx))
            ret = max(parse(idx), ret)
        return ret
