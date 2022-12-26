# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/12/26 17:03
# File: 1759.py
# Desc: 

class Solution:
    def countHomogenous(self, s: str) -> int:
        d = list()
        num = 0
        last = ''
        for i in s:
            if i == last:
                num += 1
            else:
                if num != 0: d.append(num)
                num = 1
                last = i
        d.append(num)
        ret = 0
        for num in d:
            ret += (num+1)*num//2
        return ret % (10**9+7)
