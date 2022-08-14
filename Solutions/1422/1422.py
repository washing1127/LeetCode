# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/8/14 8:45
# File: 1422.py
# Desc: 


class Solution:
    def maxScore(self, s: str) -> int:
        z = 0 if s[0] == '1' else 1
        y = s[1:].count('1')
        ret = z+y
        for i in s[1:-1]:
            if i == '0':
                z += 1
            else:
                y -= 1
            ret = max(ret, z+y)
        return ret
