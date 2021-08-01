# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/8/1 12:06
# File: 1337.py
# Desc: 

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        dic = dict()
        for idx, i in enumerate(mat):
            num = i.count(1)
            if not num in dic.keys(): dic[num] = []
            dic[num].append(idx)
        keys = sorted(list(dic.keys()))
        count = 0
        ret = list()
        for key in keys:
            for num in dic[key]:
                ret.append(num)
                count += 1
                if count == k: return ret

