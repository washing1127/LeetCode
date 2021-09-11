# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/2/8 21:54
# File: 0978.py
# Desc: 

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(set(arr)) == 1: return 1
        
        if arr[1] > arr[0]:
            st = 1
        else: st = -1

        count = 2
        max_count = count

        for i in range(2, len(arr)):
            if (arr[i-1] - arr[i-2]) * (arr[i-1] - arr[i]) > 0:
                count += 1
            else:
                if count > max_count:
                    max_count = count
                count = 2
        if count > max_count:
            max_count = count

        return max_count