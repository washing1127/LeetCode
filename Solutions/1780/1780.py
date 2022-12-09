# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/12/9 11:17
# File: 1780.py
# Desc: 


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        l = list(range(15))
        for i in range(1,16):
            l2 = itertools.combinations(l, i)
            for j in l2:
                num = 0
                for k in j:
                    num += 3**k
                if num == n: return True
        return False
