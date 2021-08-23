# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/8/23 15:38
# File: 1646.py
# Desc: 

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n <= 1: return n
        ret = [0, 1]
        for i in range(2,n+1):
            if i % 2 == 0:
                ret.append(ret[i//2])
            else:
                ret.append(ret[i//2]+ret[i//2+1])
        return max(ret)