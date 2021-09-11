# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/5/5 19:15
# File: 0740.py
# Desc: 

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        c = collections.Counter(nums)

        dps = []
        for k, v in c.items():
            c[k] = c[k] * k
            dps.append([0,0])
        
        ks = list(c.keys())
        ks.sort()
        dps[0][0] = c[ks[0]]

        for i in range(1, len(ks)):
            k = ks[i]
            if k - 1 == ks[i-1]:
                dps[i][0] = max(dps[i-1][1] + c[k], dps[i-1][0])
            else:  # 可以加这个数
                dps[i][0] = dps[i-1][0] + c[k]
            
            dps[i][1] = max(dps[i-1])
        # print(dps)
        return max(dps[-1])