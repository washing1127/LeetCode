# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/6/14 16:45
# File: 0374.py
# Desc: 

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 0
        r = n
        while l < r:
            m = (l + r) // 2
            if guess(m) == -1:
                r = m 
            elif guess(m) == 1:
                l = m + 1
            elif guess(m) == 0:
                return m 
        return l
