# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/11/15 11:08
# File: 1710.py
# Desc: 


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1],reverse=True)
        ret = 0
        while truckSize and boxTypes:
            a,b = boxTypes.pop(0)
            if truckSize > a:
                truckSize -= a
                ret += a*b
            else:
                ret += truckSize*b
                truckSize = 0
        return ret
