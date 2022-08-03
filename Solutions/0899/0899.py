# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/8/3 11:16
# File: 0899.py
# Desc: 

class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            ans = s
            for _ in range(len(s) - 1):
                s = s[1:] + s[0]
                ans = min(ans, s)
            return ans
        return ''.join(sorted(s))

