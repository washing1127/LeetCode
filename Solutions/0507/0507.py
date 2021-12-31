# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/12/31 12:55
# File: 0507.py
# Desc: 

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        l = 1
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                l += i
                l += num//i
        return l == num != 1
