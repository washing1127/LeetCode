# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/12/15 10:41
# File: 1945.py
# Desc: 


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        s = ''.join([str(ord(i)-96) for i in s])
        for i in range(k):
            s = sum([int(i) for i in s])
            s = str(s)
        return int(s)
