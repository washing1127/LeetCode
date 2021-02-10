# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/2/10 12:27
# File: 0567.py
# Desc: 

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1=collections.Counter(s1)
        length = len(s1)
        for i in range(len(s2)-length+1):
            sub_s = s2[i:i+length]
            c2 = collections.Counter(sub_s)
            if c2 == c1:
                return True
        return False