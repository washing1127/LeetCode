# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/9/13 12:08
# File: 0447.py
# Desc: 

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ret = 0
        for p1 in points:
            dic = dict()
            for p2 in points:
                dis = (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2
                if not dis in dic.keys(): dic[dis] = 1
                else: dic[dis] += 1
            for v in dic.values():
                ret += v * (v-1)
        return ret
