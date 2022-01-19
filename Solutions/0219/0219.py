# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/1/19 10:24
# File: 0219.py
# Desc: 

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0: return False
        c = set(nums[:k])
        if len(c) < len(nums[:k]): return True
        # print(c)
        for i in range(k, len(nums)):
            num = nums[i]
            if num in c: return True
            else: 
                c.remove(nums[i-k])
                c.add(num)
            # print(c)
        return False
