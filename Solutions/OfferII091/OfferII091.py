# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/6/25 10:51
# File: OfferII091.py
# Desc: 

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp = []
        for a,b,c in costs:
            if not dp: dp.append([a,b,c])
            else:
                lo = dp[-1]
                ln = [a,b,c]
                lo2 = sorted(lo)
                min_idx = lo.index(lo2[0])
                for i in range(3):
                    if i == min_idx:
                        ln[i] += lo2[1]
                    else:
                        ln[i] += lo2[0]
                dp.append(ln)
        return min(dp[-1])
