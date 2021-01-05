# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/1/5 18:11
# File: 0830.py
# Desc: 

class Solution:
    def largeGroupPositions(self, s: str) -> list:
        char = ''
        ret = []
        st = 0
        et = 0
        for idx, c in enumerate(s):
            if c != char:
                if et - st >= 2:
                    ret.append([st, et])
                st = idx
                char = c
            else:
                et = idx
        if et - st >= 2:
            ret.append([st, et])
        return ret