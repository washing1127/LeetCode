# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/4/28 10:06
# File: 0633.py
# Desc: 
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        boundary = int(math.sqrt(c / 2))
        for i in range(boundary+1):
            ans = math.sqrt(c - i ** 2)
            if ans == int(ans): return True
        return False