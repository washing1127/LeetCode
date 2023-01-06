# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2023/3/6 20:21
# File: 2180.py
# Desc: 


class Solution:
    def countEven(self, num: int) -> int:
        ret = 0
        for i in range(2, num+1):
            if sum([int(i) for i in list(str(i))]) % 2 == 0:
                ret += 1
        return ret
