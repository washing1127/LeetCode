# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/3/7 12:55
# File: 0504.py
# Desc: 

class Solution:
    def convertToBase7(self, num: int) -> str:
        if not num: return '0'
        ret = ''
        if num >= 0:
            fh = ''
        else:
            fh = '-'
            num = abs(num)
        while num:
            ret =  str(num % 7) + ret
            num //= 7
        return fh+ret
