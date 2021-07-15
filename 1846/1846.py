# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/7/15 10:21
# File: 1846.py
# Desc: 
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1
        cur = 1
        for i in range(1, len(arr)):
            if arr[i] >= cur+1:
                cur += 1
                arr[i] = cur
        print(arr)
        return arr[-1]