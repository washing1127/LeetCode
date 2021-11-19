# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/11/19 13:52
# File: 0397.py
# Desc: 

class Solution:
    def integerReplacement(self, n: int) -> int:
        ret = 0
        l = [n]
        while 1 not in l:
            new_l = []
            for i in l:
                if i % 2 == 0:
                    new_l.append(i >> 1)
                else:
                    new_l.append(i - 1)
                    new_l.append(i + 1)
            l = new_l
            ret += 1
        return ret
