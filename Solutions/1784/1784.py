# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/10/3 11:17
# File: 1784.py
# Desc: 


class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        # return sum([1 if i else 0 for i in s.split('0')]) <= 1
        # return '0' not in s.strip('0')
        flag = True
        for i in s:
            if i == '1':
                if not flag: return False
            else:
                flag = False
        return True
