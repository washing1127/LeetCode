# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/10/13 10:48
# File: 0769.py
# Desc: 

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        # ret = 0
        # li = []
        # l = 0
        # for idx,i in enumerate(arr):
        #     li.append(i)
        #     if l == min(li) and idx == max(li):
        #         ret += 1
        #         li = []
        #         l = idx+1
        #     # print(li, l, idx)
        # return ret
        ret = 0
        mi = n
        ma = 0
        l = 0
        for idx, i in enumerate(arr):
            ma = max(i, ma)
            mi = min(i, mi)
            if mi == l and ma == idx: 
                ret += 1
                l = idx+1
                mi = n
            # else:
        return ret
