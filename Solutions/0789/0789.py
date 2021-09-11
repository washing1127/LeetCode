# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/8/22 12:03
# File: 0789.py
# Desc: 

class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        t1, t2 = target
        dis = abs(t1) + abs(t2)
        # print(dis)
        for a, b in ghosts:
            num = abs(a-t1) + abs(b-t2)
            # print([a,b], num)
            if num <= dis: return False
        return True