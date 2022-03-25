# coding=utf-8
# /usr/bin/env python
"""
Author：washing
date：2022/3/25 10:20
desc:
"""
class Solution:
    def trailingZeroes(self, n: int) -> int:
        num = 1
        for i in range(1,n+1):
            num*=i
        num = str(num)
        return len(num) - len(num.strip('0'))
