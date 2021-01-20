# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/1/20 16:04
# File: 0122.py
# Desc: 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        if not prices: return 0
        b = a = prices[0]
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                b = prices[i+1]
            else:
                total += b-a
                a = b = prices[i+1]
        if b > a: total += b-a

        return total 