# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/3/4 19:03
# File: 0300.py
# Desc: 


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        d = []
        for n in nums:
            if not d or n > d[-1]:
                d.append(n)
            else:
                l, r = 0, len(d) - 1
                loc = r
                while l <= r:
                    mid = (l + r) // 2
                    if d[mid] >= n:
                        loc = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                d[loc] = n
        return len(d)