# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/2/14 10:24
# File: 0765.py
# Desc: 

class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        count = 0
        for idx in range(0,len(row),2):
            num = row[idx]
            mate = num - 1 if num % 2 else num + 1
            mate_idx = row.index(mate)
            if mate_idx != idx + 1:
                row[idx+1], row[mate_idx] = row[mate_idx], row[idx+1]
                count += 1
        return count