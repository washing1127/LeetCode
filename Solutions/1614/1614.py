# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/1/7 10:09
# File: 1614.py
# Desc: 

class Solution:
    def maxDepth(self, s: str) -> int:
        l = 0
        ret = 0
        for i in s:
            if i == "(":
                l += 1
                ret = max(ret, l)
            elif i == ")":
                l -= 1
        return ret
