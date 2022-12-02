# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/12/2 10:17
# File: 1769.py
# Desc: 


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        d = {'0':[],'1':[]}
        for idx,c in enumerate(boxes):
            d[c].append(idx)
        ret = []
        for idx in range(len(boxes)):
            num = 0
            for idx2 in d['1']: num += abs(idx2-idx)
            ret.append(num)
        return ret
