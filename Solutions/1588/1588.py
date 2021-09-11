# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/8/29 10:33
# File: 1588.py
# Desc: 

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        s = 0
        n = len(arr)
        for i in range(n):
            lc = i 
            rc = n-i-1
            lo = (lc+1)//2
            ro = (rc+1)//2
            le = lc//2+1
            re = rc//2+1
            s += arr[i]*(lo*ro+re*le)
        return s