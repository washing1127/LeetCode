# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2023/1/29 20:21
# File: 2315.py
# Desc: 


class Solution:
    def countAsterisks(self, s: str) -> int:
        ret = 0
        s = s.split("|")
        for i in s[::2]:
            ret += i.count("*")
        return ret
