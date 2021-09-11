# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/7/13 10:31
# File: 0218.py
# Desc: 

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        pos_height = []
        for l, r, height in buildings:
            pos_height.append((l, -1 * height))
            pos_height.append((r, height))
        
        pos_height.sort(key = lambda x: (x[0],  x[1]))

        cur_handle = [0]
        pre_max_height = 0
        cur_max_height = 0

        res = []
        for pos, height in pos_height:
            if height < 0:
                cur_handle.append(-1 * height)
            else:
                cur_handle.remove(height)
            cur_max_height = max(cur_handle)
            if pre_max_height != cur_max_height:
                res.append([pos, cur_max_height])
                pre_max_height = cur_max_height
        return res
