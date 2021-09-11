# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/4/17 23:36
# File: 0220.py
# Desc: 

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0:   return False        

        from sortedcontainers import SortedList
        window = SortedList()

        for i,num in enumerate(nums):
            idx = window.bisect_left(num - t)
            if idx < len(window) and window[idx] <= (num + t):
                return True

            window.add(num)
            if i >= k:
                window.remove(nums[i-k])

        return False
