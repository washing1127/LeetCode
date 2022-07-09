# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/7/9 16:04
# File: 0873.py
# Desc: 


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        s = set(arr)
        ret = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                l = 2
                a = arr[i]
                b = arr[j]
                # if a == 4 and b == 14: print("========")
                while a + b in s:
                    a, b = b, a+b
                    l += 1
                if l > 2: ret = max(ret, l)
        return ret
