# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/9/1 10:23
# File: 1475.py
# Desc: 


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ret = []
        for idx1,i in enumerate(prices):
            for idx2 in range(idx1+1,len(prices)):
                if prices[idx2] <= i:
                    ret.append(i-prices[idx2])
                    break
            else: ret.append(i)
        return ret
