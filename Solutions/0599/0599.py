# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/3/14 10:40
# File: 0599.py
# Desc: 

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d1 = {}
        d2 = {}
        for idx, s in enumerate(list1):
            if s not in d1: d1[s] = idx
        for idx, s in enumerate(list2):
            if s not in d2: d2[s] = idx
        minimum = 2000
        ret = []
        if len(list1) > len(list2): d1,d2 = d2,d1
        for k,v1 in d1.items():
            if k not in d2: continue
            v2 = d2[k]
            if v1+v2 == minimum: ret.append(k)
            elif v1+v2 < minimum:
                ret = [k]
                minimum = v1+v2
        return ret
