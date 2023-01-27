# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2023/01/27 20:21
# File: 2309.py
# Desc: 



class Solution:
    def greatestLetter(self, s: str) -> str:
        ret = ''
        for i in 'abcdefghijklmnopqrstuvwxyz':
            if i in s and i.upper() in s:
                ret = i.upper()
        return ret
