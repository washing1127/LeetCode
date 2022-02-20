# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/2/20 16:39
# File: 0717.py
# Desc: 

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        s = ''.join([str(i) for i in bits])
        while len(s) > 1:
            if s[0] == '1': s = s[2:]
            else: s = s[1:]
            # print(s)
        return s == '0'
