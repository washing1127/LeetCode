# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2023/1/20 21:37
# File: 1817.py
# Desc: 

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k2: int) -> List[int]:
        d = dict()
        for k,v in logs:
            if not k in d: d[k] = set()
            d[k].add(v)
        ret = [0] * k2
        for v in d.values():
            ret[len(v)-1] += 1
        return ret
