# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/12/21 11:00
# File: 1154.py
# Desc: 

class Solution:
    def dayOfYear(self, date: str) -> int:
        l = [31,28,31,30,31,30,31,31,30,31,30,31]
        def rn(num):
            if num % 100 == 0:
                if num % 400 == 0: return True
                return False
            if num % 4 == 0:
                return True
            return False
        y,m,d=date.split("-")
        if rn(int(y)): l[1] = 29
        return sum(l[:int(m)-1])+int(d)
