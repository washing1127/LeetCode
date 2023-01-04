# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/1/4 10:50
# File: 1802.py
# Desc: 



class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        top = (n+1)*n//2
        if top >= n: top = 0
        rest = (maxSum-top) - n + top
        su = 0
        height = (maxSum-top) // n
        # print(height,rest)
        while su < rest:
            lidx = max(index - height, 0)
            ridx = min(index + height, n-1)
            ll = index - lidx + 1
            rl = ridx - index + 1
            suml = (height * 2 - ll + 1) * ll // 2
            sumr = (height * 2 - rl + 1) * rl // 2
            # print(suml, height, sumr)
            su = suml + sumr - height
            if su > rest: break
            height += 1
            # print(lidx, index, ridx, height, su, rest)
        return height
