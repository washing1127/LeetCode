# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/3/31 10:15
# File: 0728.py
# Desc: 

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def ck(num):
            s = str(num)
            if '0' in s: return False
            for i in s:
                if num % int(i) != 0: return False
            return True
        ret = []
        for i in range(left, right+1):
            if ck(i): ret.append(i)
        return ret
