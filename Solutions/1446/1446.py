# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/12/1 10:26
# File: 1446.py
# Desc: 

class Solution:
    def maxPower(self, s: str) -> int:
        last = ""
        longest = 0
        counter = 0
        for i in s:
            if i == last:
                counter += 1
            else:
                last = i 
                counter = 1
            longest = max(counter, longest)
        return longest
