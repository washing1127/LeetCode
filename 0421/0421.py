# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/5/16 16:51
# File: 0421.py
# Desc: 

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        HIGH_BIT = 30

        x = 0
        for k in range(HIGH_BIT, -1, -1):
            seen = set()
            for num in nums:
                seen.add(num >> k)

            x_next = x * 2 + 1
            found = False
            
            for num in nums:
                if x_next ^ (num >> k) in seen:
                    found = True
                    break

            if found:
                x = x_next
            else:
                x = x_next - 1
        
        return x
