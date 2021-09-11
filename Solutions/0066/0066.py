# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/1/12 09:39
# File: 0066.py
# Desc: 
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        more = 0
        for i in range(len(digits)-1, -1, -1):
            num = digits[i]
            if num == 9: 
                more = 1
                digits[i] = 0
            else: 
                digits[i] = num + 1
                return digits
        if more:
            digits.insert(0, 1)
        return digits