# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/2/23 19:22
# File: 1052.py
# Desc: 

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        count = 0
        rest = 0
        max_rest = 0
        left = 0
        for i in range(len(customers)):
            if i >= X:
                if grumpy[left] == 1:
                    rest -= customers[left]
                left += 1
            if grumpy[i] == 0:
                count += customers[i]
            else:
                rest += customers[i]
            if rest > max_rest: max_rest = rest

        return count + max_rest