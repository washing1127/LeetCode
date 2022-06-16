# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/6/16 10:22
# File: 0532.py
# Desc: 


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        c = collections.Counter(nums)
        keys = list(c.keys())
        keys.sort()
        ret = 0
        i = 0
        j = 0
        while True:
            old_i = i
            # print(i,j,len(keys))
            if keys[j] - keys[i] == k:
                if i == j: ret += 1 if c[keys[i]] > 1 else 0
                else: ret += 1
                i += 1
                j += 1
            elif keys[j] - keys[i] < k:
                j += 1
            else:
                i += 1
            if i >= len(keys): return ret
            elif j >= len(keys):
                j -= 1
                if i == old_i:
                    return ret

