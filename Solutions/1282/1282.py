# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/8/12 20:28
# File: 1282.py
# Desc: 

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = dict()
        ret = []
        for idx, size in enumerate(groupSizes):
            if not size in d: d[size] = []
            d[size].append(idx)
            if len(d[size]) == size:
                ret.append(d[size])
                d[size] = []
        return ret
