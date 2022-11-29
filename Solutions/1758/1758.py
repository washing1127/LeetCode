# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/11/29 17:03
# File: 1758.py
# Desc: 


class Solution:
    def minOperations(self, s: str) -> int:
        ret1 = ret2 = 0
        ta = '0'
        tb = '1'
        for i in s:
            if i != ta:
                ret1 += 1
            ta = '0' if ta == '1' else '1'
            if i != tb:
                ret2 += 1
            tb = '0' if tb == '1' else '1'
        return min(ret2, ret1)
