# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2020/6/18 10:35
# File: 0483.py
# Desc: 

class Solution:
    def smallestGoodBase(self, n: str) -> str:
        num = int(n)
        for m in range(num.bit_length(),2,-1):
            x = int(pow(num,1/(m-1)))
            if num == (pow(x,m) - 1)//(x-1):
                return str(x)
        return str(num-1)
