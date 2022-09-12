# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/9/13 06:00
# File: 0670.py
# Desc: 


class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        s2=sorted(s,reverse=True)
        for idx, (a,b) in enumerate(zip(s,s2)):
            if a != b:
                s[''.join(s).rfind(b)] = a
                s[idx] = b
                return int(''.join(s))
        return num
