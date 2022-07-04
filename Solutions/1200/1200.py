# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/7/4 12:07
# File: 1200.py
# Desc: 


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ret = []
        for i in range(1,len(arr)):
            a,b = arr[i-1], arr[i]
            if not ret or ret[0][1] - ret[0][0] == b-a: ret.append([a,b])
            elif ret[0][1] - ret[0][0] > b-a: ret = [[a,b]]
        return ret
